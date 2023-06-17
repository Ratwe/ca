import numpy as np

# Параметры задачи
xa = 0.0
xb = 1.0
ya = 1.0
yb = 3.0

N = 10
h = 1 / N


# Первое слагаемое для аппроксимации второй производной разностным аналогом
def term(x, y):
    return (y[x - 1] - 2 * y[x] + y[x + 1]) / (h ** 2)


# Получение списка значений функции во всех точках
def F(y):
    f = np.zeros(N + 1)

    f[0] = y[0] - ya
    f[N] = y[N] - yb

    for i in range(1, N):
        f[i] = term(i, y) - y[i] ** 3 - (i * h) ** 2  # Аппроксимируем вторую производную разностным аналогом

    return f


def x_delta_by_gauss(J, b):
    return np.linalg.solve(J, b)


def x_plus_1(x_delta, x_previous):
    x_next = x_previous + x_delta

    return x_next


def newton_method(x_init):
    first = x_init[0]

    second = x_init[1]

    third = x_init[2]

    jacobian = jacobian_exercise(first, second, third)

    vector_b_f_output = function_exercise(first, second, third)

    x_delta = x_delta_by_gauss(jacobian, vector_b_f_output)

    x_plus_1 = x_delta + x_init

    return x_plus_1


def iter_newton(X, function, jacobian, imax=1e6, tol=1e-5):
    for i in range(int(imax)):
        J = jacobian(X)  # calculate jacobian J = df(X)/dY(X)
        Y = function(X)  # calculate function Y = f(X)
        dX = np.linalg.solve(J, Y)  # solve for increment from JdX = Y
        X -= dX  # step X by dX
        if np.linalg.norm(dX) < tol:  # break if converged
            print('converged.')
            break
    return X


# разностная сетка
x = np.linspace(xa, xb, N + 1)
print(x)

# print (iterative_newton([1,2]))
print(list(map(float, (iterative_newton(x)))))
