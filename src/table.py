from point_struct import Point


# Ищем индекс ближайшего к Х значения в таблице
def get_index(table, x):
    diff = abs(table[0].x - x)
    index = 0

    for i in range(len(table)):
        if abs(table[i].x - x) < diff:
            diff = abs(table[i].x - x)
            index = i

    return index


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
