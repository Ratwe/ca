from newton import *
from table import *

filename = "../data/data.txt"
init_table = read_table(filename)
print("Исходная таблица:")
print_table(init_table)

n = 3  # n = int(input("Введите степень n аппроксимирующих полиномов: "))
x = 0.52  # x = float(input("Введите значение аргумента x, для которого выполняется интерполяция: "))
index = get_index(init_table, x)
table = get_bordered_table(init_table, index, n + 1)
print("Минимизированная таблица для расчётов:")
print_table(table)

diff_table = get_diff_table(table, n)
print("Таблица разделённых разностей:")
print_diff_table(diff_table, n)

newton_polynom = newton_calc(diff_table, n, x)
print("Полином Ньютона: {:.5f}".format(newton_polynom))