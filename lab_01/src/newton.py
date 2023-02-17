# Какие точки будем использовать для аппроксимации
import numpy


def get_bordered_table(table, index, n):
    left = index
    right = index

    # при чётном - опускаем границу
    # при нечётном - поднимаем
    for i in range(n - 1):
        if i % 2:
            if left == 0:
                right += 1
            else:
                left -= 1
        else:
            if right == len(table) - 1:
                left -= 1
            else:
                right += 1

    return table[left:right + 1]


# Таблица разделённых разностей
def get_diff_table(table, n, mode = 0):
    row_shift = 2  # всегда есть 2 столбца X и Y: начинаем добавлять с 3-го
    if not mode:
        diff_table = []
        for point in table:
            diff_table.append([point.x, point.y])  # заполняем таблицу стартовыми координатами

    # транспонируем, чтобы в первом ряду были Х, а во втором - Y
    # т.к. без этого diff_table =
    # [[0.3, 0.655336], [0.45, 0.450447], [0.6, 0.225336], [0.75, -0.01831]]
    # а надо
    # [[ 0.3       0.45      0.6       0.75    ]
    #  [ 0.655336  0.450447  0.225336 -0.01831 ]]

    if mode:
        diff_table = table

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


def newton_calc(diff_table, n, z):
    row_shift = 2
    res = diff_table[1][0]  # столбец Y, верхняя строка
    left_part = 1

    for i in range(n):
        left_part *= (z - diff_table[0][i])  # высчитываем Z - Y(Z)
        res += left_part * diff_table[i + row_shift][0]  # Y в i-й степени, а строка нулевая, тк её всегда берём

    # print(f"newton_calc при z = {z}: {res}")
    return res
