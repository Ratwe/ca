import numpy

EPS = 1e-8


def equal(a, b):
    return abs(a - b) < EPS


def get_diff_table(table, mode = 0):
    diff_table = []
    row_shift = 2

    if not mode:
        # дублируем точки
        for point in table:
            diff_table.append([point.x, point.y])  # заполняем таблицу стартовыми координатами
            diff_table.append([point.x, point.y])

        diff_table = list([list(row) for row in numpy.transpose(diff_table)])

        # Добавляем столбец первых производных
        yd_row = []
        x_row = diff_table[0]
        y_row = diff_table[1]
        ind = 2

        for point in table:
            yd_row.append(point.derivative)
            if ind < len(x_row):
                yd_row.append((y_row[ind - 1] - y_row[ind]) / (x_row[ind - 1] - x_row[ind]))
                ind += 2
        diff_table.append(yd_row)

    if mode:
        diff_table = table
    x_row = diff_table[0]

    # Высчитываем и заполняем другие столбцы таблицы разности
    for i in range(row_shift, len(x_row)):
        diff_table.append([])
        # мы заполняем ПОСЛЕДНИЙ столбец, поэтому черпаем значения из ПРЕДПОСЛЕДНЕГО
        cur_y_row = diff_table[len(diff_table) - 2]  # начинаем с y_row
        # Добавим элемент проходом сверху вниз
        for j in range(0, len(x_row) - i):
            # Если точки совпадают - пишем производную
            if equal(x_row[j], x_row[j + i]):
                cur = yd_row[j]
            else:
                cur = (cur_y_row[j] - cur_y_row[j + 1]) / (x_row[j] - x_row[j + i])
            diff_table[i + row_shift - 1].append(cur)  # в новый пустой столбец пишем массив

    return diff_table


def hermit_calc(diff_table, n, z):
    row_shift = 2
    res = diff_table[1][0]  # столбец Y, верхняя строка
    left_part = 1

    for i in range(n):
        left_part *= (z - diff_table[0][i])  # высчитываем Z - Y(Z)
        res += left_part * diff_table[i + row_shift][0]  # Y в i-й степени, а строка нулевая, тк её всегда берём

    return res
