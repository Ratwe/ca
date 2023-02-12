from src import newton
from src.newton import newton_calc


def get_system_table():
    table = []
    file = open("../data/system1.txt")

    for line in file.readlines():
        row = list(map(float, line.split(" ")))
        table.append([row[0], row[1], None])

    file = open("../data/system2.txt")

    for line in file.readlines():
        row = list(map(float, line.split(" ")))
        table.append([row[0], None, row[1]])

    table.sort()

    file.close()
    return table


# Дополним таблицу
def complement_table(table):
    n = 3
    # таблицы разностей по данным 0 и (1 или 2) строк
    table1 = []
    table2 = []
    for i in range(len(table)):
        if table[i][1] is not None:
            table1.append([table[i][0], table[i][1]])
        else:
            table2.append([table[i][0], table[i][2]])

    diff_table1 = newton.get_diff_table(table1, n, 1)
    diff_table2 = newton.get_diff_table(table2, n, 1)

    for i in range(len(table)):
        if table[i][2] is None:
            table[i][2] = newton_calc(diff_table2, n, table[i][0])
        if table[i][1] is None:
            table[i][1] = newton_calc(diff_table1, n, table[i][0])

    return table


def search_system_root():
    table = get_system_table()
    print("system_table", table)

    table = complement_table(table)
    print("completed_table", table)
