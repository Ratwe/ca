import numpy

from src import newton
from src.newton import newton_calc
from src.table import print_diff_table

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


def get_root_table(root_table, n):
    row_shift = 2
    x_row = root_table[0]

    # Добавляем столбцы в таблицу
    for i in range(1, n + 1):
        root_table.append([])
        cur_y_row = root_table[i]

        for j in range(n - i + 1):
            cur = (cur_y_row[j] - cur_y_row[j + 1]) / (x_row[j] - x_row[j + i])
            root_table[i + row_shift - 1].append(cur)

    return root_table


def change_axis(table, n):
    for i in range(n + 1):
        table[i][0], table[i][1] = table[i][1], table[i][0]

    return table


def search_newton_root(table, n):
    if change_sign(table, n) == NOT_CHANGE:
        print("Функция не имеет корней!")
    else:
        root_table = []
        for point in table:
            root_table.append([point.x, point.y])  # заполняем таблицу стартовыми координа

        root_table = change_axis(root_table, n)
        root_table = list([list(row) for row in numpy.transpose(root_table)])
        root_table = get_root_table(root_table, n)

        print("Таблица для обратной интерполяции:")
        print_diff_table(root_table, n + 1)

        print("Вычисленный корень (Ньютон): {:.5f}".format(newton_calc(root_table, n, 0)))