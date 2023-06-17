import numpy as np


def f(x):
    return (1 / math.sqrt(2 * math.pi)) * math.exp(-(x ** 2) / 2)


def simpson(xCur):
    steps = 1000
    step = xCur / (steps * 2)

    xValues = np.array([i * step for i in range(steps * 2 + 1)])
    funcValues = np.array([f(x_i) for x_i in xValues])

    sumX1 = 4 * np.sum([funcValues[2 * i - 1] for i in range(1, steps)])
    sumX2 = 2 * np.sum([funcValues[2 * i] for i in range(1, steps - 1)])

    return (step / 3) * (funcValues[0] + funcValues[-1] + sumX1 + sumX2)


import math


def newton_method(f, df, eps=1e-6):
    """
    Решает нелинейное уравнение f(x) = 0
    с помощью метода Ньютона.
    f - функция, для которой ищется корень
    df - производная функции f
    x0 - начальное приближение

    Возвращает корень уравнения
    """

    max_iter = 1000
    x = 0.5

    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < eps:
            return x
        dfx = df(x)
        if dfx == 0:
            break
        x = x - fx / dfx
    return None


# Пример использования функции newton_method
# Решение уравнения x^2 - 2 = 0
f = lambda x: x ** 2 - 2
df = lambda x: 2 * x
x0 = 1.0
root, num_iter = newton_method(f, df, x0)
if root is not None:
    print(f"Корень уравнения: {root}")
    print(f"Число итераций: {num_iter}")
else:
    print("Решение не найдено.")


def bin_search(value):
    eps = 1e-3
    left = 0
    right = 1

    while value > simpson(right):
        left = right
        right *= 2

    while right - left > eps:
        midX = (right + left) / 2

        if value < simpson(midX):
            right = midX
        else:
            left = midX

    return left


y = float(input("Enter y value: "))

ans = bin_search(y)

print(f"Answer is {ans:.5f}")
