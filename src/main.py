from newton import *
from table import *

filename = "../data/data.txt"
init_table = read_table(filename)
print_table(init_table)

n = int(input("Введите степень n аппроксимирующих полиномов: "))
x = float(input("Введите значение аргумента x, для которого выполняется интерполяция: "))
index = get_index(init_table, x)
table = get_bordered_table(init_table, index, n)
print_table(table)