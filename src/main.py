from newton import *
from src import newton, hermit
from src.hermit import hermit_calc
from table import *

filename = "../data/data2.txt"
init_table = read_table(filename)
print("Исходная таблица:")
print_table(init_table)

n = 3  # n = int(input("Введите степень n аппроксимирующих полиномов: "))
x = 0.5  # x = float(input("Введите значение аргумента x, для которого выполняется интерполяция: "))
index = get_index(init_table, x)
table = get_bordered_table(init_table, index, n + 1)
print("Минимизированная таблица для расчётов:")
print_table(table)

diff_table = newton.get_diff_table(table, n)
print("Таблица разделённых разностей:")
print_diff_table(diff_table, n + 1)

newton_polynom = newton_calc(diff_table, n, x)
print("Полином Ньютона: {:.5f}".format(newton_polynom))

diff_table = hermit.get_diff_table(table)
print("Таблица разделённых разностей:")
print_diff_table(diff_table, 2 * len(table))

hermit_polynom = hermit_calc(diff_table, n, x)
print("Полином Эрмита: {:.5f}".format(hermit_polynom))