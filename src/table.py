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
    print("+" + "-" * 7 + ("+" + "-" * 12) * 3 + "+")
