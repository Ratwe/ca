import prettytable as pt
import matplotlib.pyplot as plt
from gaus import integral_by_gauss, solve_ls_by_gaus_method
from derivative import *
from math import log, exp

task = int(input("Введите номер задания: "))

if task == 1:
    epsilon = 1e-3
    max_dot_count = 13
    f_1 = lambda x: 1 - x
    f_2 = lambda x: 0

    with open("./data.txt", "r") as file:
        xs = list(map(float, file.readline().split('\t')[1:]))
        ys = []
        zs = []

        for line in file:
            line = list(map(float, line.split('\t')))
            ys.append(line[0])
            zs.append(line[1:])

            for i in range(len(zs[-1])):
                zs[-1][i] = log(zs[-1][i])

        matrix = [[1, xs[0], ys[0], zs[0][0]], [1, xs[-1], ys[-1], zs[-1][-1]],[1, xs[0], ys[-1], zs[-1][0]]]

        result_coef = solve_ls_by_gaus_method(matrix)
        function = lambda x, y: result_coef[0] + result_coef[1] * x + result_coef[2] * y
        real_value = lambda x, y: exp(function(x, y))

        result_x = []

        for i in range(1, max_dot_count + 1):
            result_x.append(integral_by_gauss(min(xs), max(xs), i, max_dot_count, real_value, f_2, f_1, epsilon))

        result_y = []

        for i in range(1, max_dot_count + 1):
            result_y.append(integral_by_gauss(min(xs), max(xs), max_dot_count, i, real_value, f_2, f_1, epsilon))

        print(result_x)
        print(result_y)

        plt.grid()
        plt.plot([i for i in range(1, max_dot_count + 1)], result_x, label="Изменение количества узлов по направлению x")
        plt.plot([i for i in range(1, max_dot_count + 1)], result_y, label="Изменение количества узлов по направлению y")
        plt.legend()
        plt.show()
else:

    step_1 = 1
    step_2 = 2
    p = 2
    ys = [0.571, 0.889, 1.091, 1.231, 1.333, 1.412]
    xs = [i + 1 for i in range(6)]

    table = pt.PrettyTable()
    columns = ["x", "y", "1", "2", "3", "4", "5"]

    table.add_column(columns[0], xs)
    table.add_column(columns[1], ys)

    buffer_c = []
    buffer_l = []
    buffer_l_2 = []

    # Разностные

    for i in range(1, len(xs)):
        buffer_l.append(one_side_left_dif_derivative(step_1, ys[i], ys[i - 1]))

    buffer_l.insert(0, one_side_left_dif_derivative(step_1, ys[0]))

    for i in range(1, len(xs) - 1):
        buffer_c.append(center_dif_derivative(step_1, ys[i + 1], ys[i - 1]))

    buffer_c.insert(0, center_dif_derivative(0))
    buffer_c.append("None")

    for i in range(step_2, len(xs)):
        buffer_l_2.append(one_side_left_dif_derivative(step_2, ys[i], ys[i - step_2]))

    # Рунге

    buffer_runge = []

    for i in range(2, len(buffer_l)):
        buffer_runge.append(second_runge_formula(float(buffer_l[i]), float(buffer_l_2[i - step_2]), int(step_2 / step_1), p))

    buffer_runge.insert(0, "None")
    buffer_runge.insert(0, "None")

    # Выравнивающие

    xsi = [ x for x in xs ]
    teta = [xs[i] / ys[i] for i in range(len(xs))]

    buffer_align = []

    for i in range(len(xs) - 1):
        buffer_align.append(derivative_with_align_vars(teta[i], teta[i + 1], xsi[i], xsi[i + 1], ys[i], xs[i]))

    buffer_align.append("None")

    # Вторая разностная

    buffer_second = []

    for i in range(1, len(xs) - 1):
        buffer_second.append(second_dif_derivative(step_1, ys[i + 1], ys[i], ys[i - 1]))

    buffer_second.insert(0, center_dif_derivative(0))
    buffer_second.append("None")

    table.add_column("1", buffer_l)
    table.add_column("2", buffer_c)
    table.add_column("3", buffer_runge)
    table.add_column("4", buffer_align)
    table.add_column("5", buffer_second)

    print(table)








