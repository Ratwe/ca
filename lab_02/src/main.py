# Импортирование необходимых модулей и функций
from polynom import *
from spline import *
from read import *

# Чтение таблицы точек из файла
pointTable = readTable("../data/data.txt")

# Вывод таблицы точек
printTable(pointTable)

# Задание степени полинома
n = 3

# Ввод значения x
x0 = float(input("Введите x: "))

# Инициализация переменных для подсчета производных
start1 = 0
end1 = 0
start2 = 0
end2 = 0
start3 = 0
end3 = 0

# Инициализация списков значений y для каждого метода
yValues = [list(), list(), list(), list()]


# Проверка, достаточно ли точек для вычисления полинома заданной степени
if n < len(pointTable):
    print("Newton =", newton_polynomial(pointTable, n + 1, x0))
    # Вычисление значения производной в конечной точке для вычисления сплайна 0 и P''(xn)
    end2 = find_derivative_newton_polynomial(pointTable, n + 1, pointTable[-1].x)

    # Вычисление значений производных в начальной и конечной точках для вычисления сплайна P''(x0) и P''(xn)
    start3 = find_derivative_newton_polynomial(pointTable, n + 1, pointTable[0].x)
    end3 = find_derivative_newton_polynomial(pointTable, n + 1, pointTable[-1].x)
else:
    print("Ньютон 3-й степени нельзя посчитать, ведь точек всего", len(pointTable))


# Вычисление значения сплайна 0 и 0 в точке x
print("Spline 2.1: ", spline(pointTable, x0, start1, end1))
# Вывод уравнения сплайна 0 и 0
print_spline_funct(pointTable, x0, start1, end1)
print("-----")

# Вычисление значения сплайна 0 и P''(xn) в точке x
print("Spline 2.2: ", spline(pointTable, x0, start2, end2))
# Вывод уравнения сплайна 0 и P''(xn)
print_spline_funct(pointTable, x0, start2, end2)
print("-----")

# Вычисление значения сплайна P''(x0) и P''(xn) в точке x
print("Spline 2.3: ", spline(pointTable, x0, start3, end3))
print_spline_funct(pointTable, x0, start3, end3)
print("-----")