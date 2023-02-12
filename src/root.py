import numpy

from src import newton

CHANGE = 1
NOT_CHANGE = 0


def change_sign(table, n):
    last = table[0].y

    for i in range(0, n + 1):
        cur = table[i].y

        if cur * last <= 0:
            return CHANGE

        last = cur

    return NOT_CHANGE


# def newton_interpolation(Table, SizeTable, power, argument):
#     """
#         Значение интерполяцинного полинома Ньютона
#         при заданной степени power и аргументе argument.
#         Параметры выбираются из таблицы Table размером
#         SizeTable.
#     """
#
#     Table = SortTable(Table, SizeTable)
#     Config = CreateConfig(Table, SizeTable, power, argument)
#     print(Config)
#     SplitDiff = CreateSplitDiff(Config, power)
#     result = NewtonPolynomial(Config, power, argument, SplitDiff)
#
#     return result


def search_newton_root(table, n):
    if change_sign(table, n) == NOT_CHANGE:
        print("Функция не имеет корней!")
    else:
        print("table0", table)
        table = list([list(row) for row in numpy.transpose(table)])
        print("table1", table)
        diff_table = newton.get_diff_table(table, n)
