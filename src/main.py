from newton import *
from table import *

filename = "../data/data.txt"
init_table = read_table(filename)
print_table(init_table)

n = 4  # n = int(input("Введите степень n аппроксимирующих полиномов: "))
x = 0.5  # x = float(input("Введите значение аргумента x, для которого выполняется интерполяция: "))
index = get_index(init_table, x)
table = get_bordered_table(init_table, index, n)
print_table(table)

diff_table = get_diff_table(table, n)
print_diff_table(diff_table)