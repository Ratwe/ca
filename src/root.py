import numpy

from src import newton, hermit
from src.hermit import hermit_calc
from src.newton import newton_calc
from src.table import print_diff_table

CHANGE = 1
NOT_CHANGE = 0


def change_sign(table):
    last = table[0].y

    for i in range(0, len(table)):
        cur = table[i].y

        if cur * last <= 0:
            return CHANGE

        last = cur

    return NOT_CHANGE


def change_axis(table):
    for i in range(len(table)):
        table[i][0], table[i][1] = table[i][1], table[i][0]

    return table


def search_newton_root(table, n):
    if change_sign(table) == NOT_CHANGE:
        print("Функция не имеет корней!")
    else:
        root_table = []
        for point in table:
            root_table.append([point.x, point.y])  # заполняем таблицу стартовыми координатами

        root_table = change_axis(root_table)
        root_table = newton.get_diff_table(root_table, n, 1)

        # print("Таблица для обратной интерполяции:")
        # print_diff_table(root_table, n + 1)

        print("Вычисленный корень (Ньютон): {:.5f}\n\n".format(newton_calc(root_table, n, 0)))


def add_derivatives_row(root_table, table):
    # Добавляем столбец первых производных
    yd_row = []
    x_row = root_table[0]
    y_row = root_table[1]
    ind = 2

    for point in table:
        yd_row.append(point.derivative)
        if ind < len(x_row):
            yd_row.append((y_row[ind - 1] - y_row[ind]) / (x_row[ind - 1] - x_row[ind]))
            ind += 2
    root_table.append(yd_row)

    return root_table


def search_hermit_root(table, n):
    if change_sign(table) == NOT_CHANGE:
        print("Функция не имеет корней!")
    else:
        root_table = []
        for point in table:
            root_table.append([point.x, point.y])  # заполняем таблицу стартовыми координатами
            root_table.append([point.x, point.y])

        root_table = change_axis(root_table)
        root_table = list([list(row) for row in numpy.transpose(root_table)])
        root_table = add_derivatives_row(root_table, table)
        root_table = hermit.get_diff_table(root_table, 1)

        # print("Таблица для обратной интерполяции:")
        # print_diff_table(root_table, 2 * len(table))

        print("Вычисленный корень (Эрмит): {:.5f}\n\n".format(hermit_calc(root_table, 2 * len(table) - 1, 0)))
