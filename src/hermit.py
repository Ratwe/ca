import numpy


def get_diff_table(table, n):
    row_shift = 2
    diff_table = []

    # дублируем точки n + 1 раз
    for point in table:
        for i in range(n + 1):
            diff_table.append([point.x, point.y])  # заполняем таблицу стартовыми координатами

    diff_table = list([list(row) for row in numpy.transpose(diff_table)])

    print("diff_table0:", diff_table)

    yd_row = []
    ind = n + 1
    for point in table:
        for i in range(n):
            yd_row.append(point.derivative)
        if ind < len(diff_table[0]):
            yd_row.append(diff_table[1][ind] - diff_table[1][ind - 1])
            ind += n + 1

    diff_table.append(yd_row)

    yd_row = []
    ind = n
    for point in table:
        for i in range(n):
            yd_row.append(point.derivative)
        if ind < len(diff_table[0]):
            yd_row.append(diff_table[1][ind] - diff_table[1][ind - 1])
            ind += n + 1

    diff_table.append(yd_row)

    print("diff_table1:", diff_table)

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
        subElement = (tableOfSub[i][YColId] - tableOfSub[i + 2][YColId]) / (tableOfSub[i][XColId] - tableOfSub[i + 2][XColId])
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
            if (abs(XRow[j] - XRow[j + countOfArgs]) < 1e-8):
                cur = YdRow[j]
            else:
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