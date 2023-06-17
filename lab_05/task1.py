import sympy as sym
import numpy as np
from scipy.linalg import solve

N = 3
eps = 1e-3


def Newton(F, Jacobian):
    # x = float(input("Enter the value for x: "))
    # y = float(input("Enter the value for y: "))
    # z = float(input("Enter the value for z: "))
    curValues = np.array([0.54, 0.54, 0.54], dtype=float)

    FCur = F(*curValues)  # значения функций системы уравнений при текущих значениях переменных
    JacobianCur = Jacobian(*curValues)

    delta = solve(JacobianCur, FCur).reshape((N,))  # просчёт delta из JacobianCur * delta = FCur
    curValues += delta

    while np.linalg.norm(delta) > eps:
        curValues -= delta

        FCur = F(*curValues)
        JacobianCur = Jacobian(*curValues)

        delta = solve(JacobianCur, FCur).reshape((N,))

        x, y, z = curValues
        print(f"Current values: x = {x:.7f}, y = {y:.7f}, z = {z:.7f}")

    return curValues


vars = ['x', 'y', 'z']
funcs = ['x ** 2 + y ** 2 + z ** 2 - 1',
         '2 * x ** 2 + y ** 2 - 4 * z',
         '3 * x ** 2 - 4 * y + z ** 2']

F = sym.Matrix(funcs)
print("F = ", F)  # матрица из трёх уравнений
Jacobian = sym.Matrix(funcs).jacobian(vars)
# матрица символьных выражений производных системы уравнений.

Jacobian = sym.lambdify(sym.symbols(vars), Jacobian)
# функция, которая принимает числовые значения переменных и возвращает матрицу числовых значений Якобиана.
F = sym.lambdify(sym.symbols(vars), F)  # теперь тоже принимает значения x, y, z и возвращает матрицу

values = Newton(F, Jacobian)
space = ' '

print(f"Answer is x: {values[0]:.5f}\n{space:>10}y: {values[1]:.5f}\n{space:>10}z: {values[2]:.5f}\n")