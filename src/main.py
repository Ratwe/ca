from table import *

filename = "test.txt"
table = read_table(filename)
print_table(table)

n = input("Введите степень n аппроксимирующих полиномов: ")
x = input("Введите значение аргумента x, для которого выполняется интерполяция: ")