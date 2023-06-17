import sympy as sym
import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt

N = 100
eps = 1e-3


def Newton(F, Jacobian, initValues):
    curValues = np.array(initValues, dtype="float")

    FCur = F(*curValues)
    JacobianCur = Jacobian(*curValues)

    delta = solve(JacobianCur, FCur).reshape((N + 1,))
    curValues += delta

    while np.linalg.norm(delta) > eps:
        curValues -= delta

        FCur = F(*curValues)
        JacobianCur = Jacobian(*curValues)

        delta = solve(JacobianCur, FCur).reshape((N + 1,))

    return curValues


# краевые условия
start = [0, 1]
end = [1, 3]

# вводим разностную сетку
step = (end[0] - start[0]) / N
xValues = np.array([i * step for i in range(N + 1)])

vars = [f'y{i}' for i in range(N + 1)]

# домножим уравнение на h^2, перенесём xn^2 влево
funcs = [f'{vars[i - 1]} - 2 * {vars[i]} + {vars[i + 1]} - ({step} ** 2) * ({vars[i]} ** 3 + {xValues[i]} ** 2)' for i
         in range(1, N)]
funcs.extend(['y0 - 1', f'y{N} - 3'])

F = sym.Matrix(funcs)
Jacobian = sym.Matrix(funcs).jacobian(vars)

Jacobian = sym.lambdify(sym.symbols(vars), Jacobian)
F = sym.lambdify(sym.symbols(vars), F)

delta = (end[1] - start[1]) / (end[0] - start[0])
initValues = [start[1] + delta * i * step for i in range(N + 1)]

yValues = Newton(F, Jacobian, initValues)

plt.grid()
plt.plot(xValues, initValues, label="Init values")
plt.plot(xValues, yValues, label="Result values")
plt.legend()
plt.show()

print(yValues[20:30])