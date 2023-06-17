import numpy as np
import pandas as pd
from typing import Callable as Fn, Dict, Tuple

IntegrationFn = Fn[[Fn[[float], float], float, float], float]
Point = Tuple[float, float]
RegionDict = Dict[Point, float]
from scipy.interpolate import CubicSpline as Spline

# Read table
df = pd.read_csv('data.csv')

n_points = 13

x = np.array(list(map(lambda x: x / 10, range(n_points))))  # 0, 0.1,...,n_points/10
y = np.array(list(map(lambda x: x / 10, range(n_points))))
z = df.values

print("x = ", x)
print("y = ", y)
print("z = ", z)

# Alignment variable
eta = np.array([[np.log(i) for i in zi] for zi in z])


def table_fn(x_: float, y_: float, use_eta=True):
    x_ind = list(x).index(x_)
    y_ind = list(y).index(y_)

    result = eta[y_ind][x_ind] if use_eta else z[y_ind][x_ind]

    return result


def get_gauss_rhs_coefs_for_system_of_equations(k):
    return 2 / (k + 1) if k % 2 == 0 else 0


# TODO: legendre polynome root-finding algorithm

from numpy.polynomial.legendre import Legendre


def get_legendre_polynomial_roots(n):
    return Legendre(n * [0] + [1]).roots()


def get_coefficients(legendre_polynomial_roots):
    roots = legendre_polynomial_roots
    n = len(roots)

    matrix = np.array([[t ** t_power for t in roots] for t_power in range(n)])

    values = np.array([get_gauss_rhs_coefs_for_system_of_equations(k) for k in range(n)])

    coefs = np.linalg.solve(matrix, values)

    return coefs


def integrate_gauss(func: Fn[[float], float], a: float, b: float, n=3):
    roots = get_legendre_polynomial_roots(n)
    coefs = get_coefficients(roots)

    xs = np.array(list(map(lambda t: (b - a) / 2 * t + (a + b) / 2, roots)))

    result = (b - a) / 2 * sum([coefs[i] * func(xs[i]) for i in range(len(roots))])

    return result


def integrate_simpson(func: Fn[[float], float], a: float, b: float, n=30):
    h = (b - a) / (n * 2)

    xs = np.array([a + i * h for i in range(n * 2 + 1)])
    ys = np.array([func(x) for x in xs])

    s1 = 4 * np.sum([ys[2 * i - 1] for i in range(1, n)])
    s2 = 2 * np.sum([ys[2 * i] for i in range(1, n - 1)])
    s = (h / 3) * (ys[0] + s1 + s2 + ys[-1])

    return s


# Integration region
def G(x: float, y: float):
    return x >= 0 and y >= 0 and (x + y) <= 1


def integrate_region(integrate_main: IntegrationFn,
                     integrate_Fs: IntegrationFn,
                     region_dict: RegionDict,
                     use_eta=False
                     ):
    xs = np.unique(list(map(lambda p: p[0], region_dict.keys())))
    ys = np.unique(list(map(lambda p: p[1], region_dict.keys())))

    points_by_y = lambda y: [p for p in region_dict.keys() if p[1] == y]

    Fs = []
    Ys = []

    for k in ys:
        points = points_by_y(k)
        xs = [p[0] for p in points]
        fn = [region_dict[p] for p in points]

        if len(xs) > 1:
            spline = Spline(xs, fn)

            if use_eta:
                func = lambda x: np.e ** spline(x)
            else:
                func = lambda x: spline(x)

            x_min = min(xs)
            x_max = max(xs)

            Fk = integrate_Fs(func, x_min, x_max)

            Fs.append(Fk)
            Ys.append(k)

    func = Spline(Ys, Fs)

    y_min = min(Ys)
    y_max = max(Ys)

    return integrate_main(func, y_min, y_max)


# G = lambda x, y: True
# x = np.arange(0, 1.1, 0.1)
# y = np.arange(0, 1.1, 0.1)
# table_fn = lambda x, y: 1
g_points = [(x_, y_) for y_ in y for x_ in x if G(x_, y_)]
print("g_points = ", g_points)

g_dict = dict(zip(g_points, [table_fn(*p, use_eta=True) for p in g_points]))
print("g_dict = ", g_dict)

i3 = integrate_region(integrate_simpson, integrate_gauss, g_dict, use_eta=True)

print("res = ", i3)