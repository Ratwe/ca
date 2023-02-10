import numpy as numpy

from point_struct import Point


def read_table(filename):
    table = []
    file = open(filename)

    for line in file.readlines():
        row = list(map(float, line.split(" ")))
        table.append(Point(row[0], row[1], row[2]))

    file.close()
    return table


def print_table(table):
    print("+" + "-" * 7 + ("+" + "-" * 12) * 3 + "+")
    print("| {:^5s} | {:^10s} | {:^10s} | {:^10s} |".format("№", "X", "Y", "Y\'"))
    print("+" + "-" * 7 + ("+" + "-" * 12) * 3 + "+")

    for i in range(len(table)):
        print("| {:^5d} | {:^10.3f} | {:^10.3f} | {:^10.3f} |".format(i,
                                                                      table[i].x,
                                                                      table[i].y,
                                                                      table[i].derivative))
    print("+" + "-" * 7 + ("+" + "-" * 12) * 3 + "+\n")


def print_diff_table(diff_table, n):
    length = len(diff_table)

    print(("+" + "-" * 22) * length + "+")
    print("| {:^20s} | {:^20s}".format("X", "Y"), end=' ')

    for k in range(2, length):
        print("| {:^20s}".format("Y" + "\'" * (k - 1)), end=' ')
    print("|")
    print(("+" + "-" * 22) * length + "+")

    for i in range(n + 1):
        for j in range(length):
            if j >= length - i:
                print("| {:^20s}".format(" "), end=' ')
            else:
                print("| {:^20.5f}".format(diff_table[j][i]), end=' ')
        print("|")

    print(("+" + "-" * 22) * length + "+\n")


# Таблица разделённых разностей
def get_diff_table(table, n):
    row_shift = 2  # всегда есть 2 столбца X и Y: начинаем добавлять с 3-го
    diff_table = []
    for point in table:
        diff_table.append([point.x, point.y])  # заполняем таблицу стартовыми координатами

    # транспонируем, чтобы в первом ряду были Х, а во втором - Y
    # т.к. без этого diff_table =
    # [[0.3, 0.655336], [0.45, 0.450447], [0.6, 0.225336], [0.75, -0.01831]]
    # а надо
    # [[ 0.3       0.45      0.6       0.75    ]
    #  [ 0.655336  0.450447  0.225336 -0.01831 ]]
    diff_table = list([list(row) for row in numpy.transpose(diff_table)])
    x_row = diff_table[0]

    # Добавляем столбцы в таблицу
    for i in range(1, n + 1):
        diff_table.append([])
        cur_y_row = diff_table[i]

        for j in range(n - i + 1):
            cur = (cur_y_row[j] - cur_y_row[j + 1]) / (x_row[j] - x_row[j + i])
            diff_table[i + row_shift - 1].append(cur)

    return diff_table
