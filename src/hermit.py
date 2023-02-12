import numpy

EPS = 1e-8


def equal(a, b):
    return abs(a - b) < EPS


def get_diff_table(table):
    row_shift = 2
    diff_table = []

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
            yd_row.append(y_row[ind] - y_row[ind - 1])
            ind += 2
    diff_table.append(yd_row)

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
                print(f"(cur_y_row[{j}] - cur_y_row[{j + 1}]) =", (cur_y_row[j] - cur_y_row[j + 1]))
                print(f"(x_row[{j}] - x_row[{j + i}]) =", (x_row[j] - x_row[j + i]))
                cur = (cur_y_row[j] - cur_y_row[j + 1]) / (x_row[j] - x_row[j + i])
            diff_table[i + row_shift - 1].append(cur)  # в новый пустой столбец пишем массив

    return diff_table


def HermitMethod(pointTable):
    countOfRowsOfTableData = 2
    tableOfSub = []
    [tableOfSub.append([point.x, point.y]) for point in pointTable]
    YdRow = []
    for point in pointTable:
        YdRow.append(point.derivative)
        YdRow.append(None)
    XColId = 0
    YColId = 1
    # Вставка пустых списком (будущих разностей) в 3 столбец
    for i in range(0, len(tableOfSub) * 2, 2): tableOfSub.insert(i + 1, [])
    # Копирование точек
    for i in range(0, len(tableOfSub), 2):
        tableOfSub[i + 1].append(tableOfSub[i][XColId])
        tableOfSub[i + 1].append(tableOfSub[i][YColId])
    for i in range(0, len(tableOfSub) - 2, 2):
        subElement = (tableOfSub[i][YColId] - tableOfSub[i + 2][YColId]) / (
                tableOfSub[i][XColId] - tableOfSub[i + 2][XColId])
        # if not pointTable[i + 1].isExit:
        #     continue
        # else:
        YdRow[i + 1] = subElement
    tableOfSub = list([list(row) for row in numpy.transpose(tableOfSub)])
    XRow = tableOfSub[0]
    YdRow.pop()
    tableOfSub.append(YdRow)

    # Добавление столбцов (строк в моей реализации)
    for countOfArgs in range(2, len(XRow)):
        tableOfSub.append([])
        curYRow = tableOfSub[len(tableOfSub) - countOfRowsOfTableData]
        # Добавление очередного элемента
        for j in range(0, len(XRow) - countOfArgs):
            if abs(XRow[j] - XRow[j + countOfArgs]) < 1e-8:
                cur = YdRow[j]
            else:
                print(f"(curYRow[{j}] - curYRow[{j + 1}]) =", curYRow[j] - curYRow[j + 1])
                print(f"(XRow[{j}] - XRow[{j + countOfArgs}]) =", (XRow[j] - XRow[j + countOfArgs]))
                cur = (curYRow[j] - curYRow[j + 1]) / (XRow[j] - XRow[j + countOfArgs])
            tableOfSub[countOfArgs + countOfRowsOfTableData - 1].append(cur)
    # Удаление пустого списка
    return tableOfSub


def hermit_calc(diff_table, n, z):
    row_shift = 2
    res = diff_table[1][0]  # столбец Y, верхняя строка
    left_part = 1

    for i in range(n):
        left_part *= (z - diff_table[0][i])  # высчитываем Z - Y(Z)
        res += left_part * diff_table[i + row_shift][0]  # Y в i-й степени, а строка нулевая, тк её всегда берём

    return res
