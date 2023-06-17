from math import sqrt
import numpy as np
from matplotlib import pyplot as plt

# Параметры задачи
xa = 0.0
xb = 1.0
ya = 1.0
yb = 3.0

N = 10
h = 1 / N
tol = 1e-6
max_iter = 1000


# Первое слагаемое для аппроксимации второй производной разностным аналогом
def term(x, y):
    return (y[x - 1] - 2 * y[x] + y[x + 1]) / (h ** 2)


# Получение СЛАУ
def F(y):
    f = np.zeros(N + 1)

    f[0] = y[0] - ya
    f[N] = y[N] - yb

    for i in range(1, N):
        print("y[i] =", y[i])
        f[i] = term(i, y) - y[i] ** 3 - (i * h) ** 2  # Аппроксимируем вторую производную разностным аналогом
        print("f[i] =", f[i])

    return f


# Функция для вычисления Якобиана
def J(y):
    jac = np.zeros((N + 1, N + 1))

    jac[0, 0] = 1.0
    jac[N][N] = 1.0

    for i in range(1, N):
        jac[i][i - 1] = 1.0 / (h ** 2)
        jac[i][i] = -2.0 / (h ** 2) - 3.0 * y[i] ** 2
        jac[i][i + 1] = 1.0 / (h ** 2)

    return jac


def x_delta_by_gauss(J, b):
    return np.linalg.solve(J, b)


def get_vector_norm(var_seq):
    sum = 0
    for i in range(2):
        sum += var_seq[i] ** 2

    return sqrt(sum)


def gauss(A, B):
    # Прямой ход метода Гаусса
    n = len(B)

    for i in range(n):
        # Поиск максимального элемента в столбце i
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k

        # Ставим строку с макс. числом в текущую i-ю строку
        for k in range(i, n):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp
        # меняем местами строки в системе значений B
        tmp = B[maxRow]
        B[maxRow] = B[i]
        B[i] = tmp

        # Приведение к верхнетреугольному виду
        for k in range(i + 1, n):
            c = -A[k][i] / A[i][i]
            for j in range(i, n):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]
            B[k] += c * B[i]

    # Обратный ход метода Гаусса
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = B[i]  # == B[maxRow]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]

    return x


def newton(x_init):
    jac = J(x_init)  # Вычисление якобиана СЛАУ

    func_y = F(x_init)  # Получение списка уравнений системы

    dx = gauss(jac, -func_y)  # solve for increment from JdX = Y

    print("jac =", jac)
    print("func_y =", func_y)
    print("dx =", dx)

    return x_init + dx


# Функция для решения системы нелинейных уравнений методом Ньютона
def iter_newton(x_init):
    count = 0

    x_old = x_init
    x_new = newton(x_old)

    diff = np.linalg.norm(x_old - x_new)

    while diff > tol and count < max_iter:
        count += 1
        print("count =", count)

        x_new = newton(x_old)
        diff = np.linalg.norm(x_old - x_new)
        x_old = x_new

        print(x_new)

    convergent_val = x_new

    return convergent_val


# разностная сетка
x = np.linspace(xa, xb, N + 1)
y = np.linspace(ya, yb, N + 1)  # это наше начальное приближение

# решаем систему нелинейных уравнений методом ньютона
y = iter_newton(y)

print("x\t y")
for i in range(N + 1):
    print("{:.4f}\t {:.4f}".format(x[i], y[i]))

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
