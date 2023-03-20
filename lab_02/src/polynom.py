from scipy.misc import derivative
import numpy as np

infinity = None


# Finding the index of the point closest to the target x value
def get_index(points, x):
    dif = abs(points[0].get_x() - x)
    index = 0
    for i in range(len(points)):
        if abs(points[i].get_x() - x) < dif:
            dif = abs(points[i].get_x() - x)
            index = i
    return index


# Taking the nearest working points for calculations
def get_working_points(points, index, n):
    left = index
    right = index
    for i in range(n - 1):
        if i % 2 == 0:
            if left == 0:
                right += 1
            else:
                left -= 1
        else:
            if right == len(points) - 1:
                left -= 1
            else:
                right += 1
    return points[left:right + 1]


# Calculating Newton polynomial and storing the results in a table
def newton_method(point_table):
    count_of_rows_of_table_data = 2
    table_of_sub = []
    [table_of_sub.append([point.get_x(), point.get_y()]) for point in point_table]

    table_of_sub = list([list(row) for row in np.transpose(table_of_sub)])
    x_row = table_of_sub[0]

    # Adding columns (rows in my implementation)
    for count_of_args in range(1, len(x_row)):
        table_of_sub.append([])
        cur_y_row = table_of_sub[len(table_of_sub) - count_of_rows_of_table_data]
        # Adding the next element
        for j in range(0, len(x_row) - count_of_args):
            if cur_y_row[j] == infinity and cur_y_row[j + 1] == infinity:
                cur = 1
            elif cur_y_row[j] == infinity:
                cur = cur_y_row[j + 1] / (x_row[j] - x_row[j + count_of_args])
            elif cur_y_row[j + 1] == infinity:
                cur = cur_y_row[j] / (x_row[j] - x_row[j + count_of_args])
            else:
                cur = (cur_y_row[j] - cur_y_row[j + 1]) / (x_row[j] - x_row[j + count_of_args])
            table_of_sub[count_of_args + count_of_rows_of_table_data - 1].append(cur)
    return table_of_sub


# Calculating Newton polynomial and returning the approximate value at x
def newton_polynomial(point_table, n, x):
    working_table = get_working_points(point_table, get_index(point_table, x), n)
    subs = newton_method(working_table)
    return calc_approximate_value(subs, n, x)


def find_derivative_newton_polynomial(point_table, n, x):
    working_table = get_working_points(point_table, get_index(point_table, x), n)
    subs = newton_method(working_table)

    def aprox_func(x):
        res = 0
        for i in range(len(subs)):
            res += subs[i][0] * x ** i
        return res

    y_derivative_n_2 = derivative(aprox_func, x, n=2, dx=1e-6)
    return y_derivative_n_2


# расчет конечного результат по полиному Ньютона
def calc_approximate_value(tableOfSub, n, x):
    countOfArgs = 2

    if tableOfSub[1][0] == infinity:
        sum = tableOfSub[1][1]
    else:
        sum = tableOfSub[1][0]

    mainPart = 1

    for i in range(n - 1):
        if tableOfSub[0][i] == infinity:
            print(3)
            mainPart *= x
        else:
            mainPart *= (x - tableOfSub[0][i])

        if tableOfSub[i + countOfArgs][0] != infinity:
            sum += mainPart * tableOfSub[i + countOfArgs][0]
    return sum


# вывод таблицу всех данных f(xi .... xn)
def printSubTable(subTable):
    countArray = len(subTable)
    maxLen = len(subTable[0])
    print(("+" + "-" * 22) * countArray + "+")
    print("| {:^20s} | {:^20s}".format("X", "Y"), end=' ')
    for k in range(2, countArray):
        print("| {:^20s}".format("Y" + "\'" * (k - 1)), end=' ')
    print("|")
    print(("+" + "-" * 22) * countArray + "+")

    for i in range(maxLen):
        for j in range(countArray):
            if j >= countArray - i:
                print("| {:^20s}".format(" "), end=' ')
            else:
                print("| {:^20.10f}".format(subTable[j][i]), end=' ')
        print("|")

    print(("+" + "-" * 22) * countArray + "+")
