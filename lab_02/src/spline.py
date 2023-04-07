def h(x1, x2):
    return x2 - x1


def a(x):
    return x


def c(c_i, ksi_i, teta_i):
    print(ksi_i * c_i + teta_i)
    return ksi_i * c_i + teta_i


def calc_a_values(y_values):
    # Функция для вычисления значений коэффициентов a в кубическом сплайне по значениям y
    # Возвращает список коэффициентов a
    a_values = []
    for i in range(len(y_values) - 1):
        a_values.append(y_values[i])
    return a_values


def f(y1, y2, y3, h1, h2):
    return 3 * ((y3 - y2) / h2 - (y2 - y1) / h1)


def ksi(ksi1, h1, h2):
    return - h1 / (h2 * ksi1 + 2 * (h2 + h1))


def teta(fi, teta_i, ksi_i, h1, h2):
    return (fi - h1 * teta_i) / (h1 * ksi_i + 2 * (h2 + h1))


def calc_h_values(x_values):
    h_values = []
    for i in range(1, len(x_values)):
        h_values.append(h(x_values[i], x_values[i - 1]))
    return h_values


def calc_c_values(x_values, y_values, start, end):
    size_x = len(x_values)
    c_values = [0] * (size_x - 1)
    c_values[0] = start
    c_values[1] = end

    if start == 0 and end == 0:
        ksi_values = [0, 0]
        teta_values = [0, 0]
    elif start == 0:
        ksi_values = [0, end / 2]
        teta_values = [0, end / 2]
    else:
        ksi_values = [start / 2, end / 2]
        teta_values = [start / 2, end / 2]

    for i in range(2, size_x):
        h2 = x_values[i] - x_values[i - 1]
        h1 = x_values[i - 1] - x_values[i - 2]

        fi_cur = f(y_values[i - 2], y_values[i - 1], y_values[i], h1, h2)
        ksi_cur = ksi(ksi_values[i - 1], h1, h2)
        teta_cur = teta(fi_cur, teta_values[i - 1], ksi_values[i - 1], h1, h2)

        ksi_values.append(ksi_cur)
        teta_values.append(teta_cur)

    c_values[-1] = teta_values[-1]

    for i in range(size_x - 2, 0, -1):
        c_values[i - 1] = c(c_values[i], ksi_values[i], teta_values[i])

    return c_values


def b(y1, y2, c1, c2, h):
    return (y2 - y1) / h - (h * (c2 + 2 * c1) / 3)


def d(c1, c2, h):
    return (c1 - c2) / (3 * h)


def calc_b_values(x_values, y_values, c_values):
    b_values = []
    for i in range(1, len(x_values) - 1):
        hi = x_values[i] - x_values[i - 1]
        b_values.append(b(y_values[i - 1], y_values[i], c_values[i - 1], c_values[i], hi))

    hi = x_values[-1] - x_values[-2]
    b_values.append(b(y_values[-2], y_values[-1], 0, c_values[-1], hi))

    return b_values


def calc_d_values(x_values, c_values):
    d_values = []

    size = len(x_values)

    for i in range(1, size - 1):
        hi = x_values[i] - x_values[i - 1]
        d_values.append(d(c_values[i], c_values[i - 1], hi))

    hi = x_values[-1] - x_values[-2]
    d_values.append(d(0, c_values[-1], hi))

    return d_values


def calculate_coefs_spline(x_values, y_values, start, end):
    a_values = calc_a_values(y_values)
    c_values = calc_c_values(x_values, y_values, start, end)
    b_values = calc_b_values(x_values, y_values, c_values)
    d_values = calc_d_values(x_values, c_values)

    return a_values, b_values, c_values, d_values


def find_index(x_values, x):
    size = len(x_values)
    index = 1

    while index < size and x_values[index] < x:
        index += 1

    return index - 1


def count_polynom(x, x_values, index, coefs):
    h = x - x_values[index]
    y = 0

    for i in range(4):
        y += coefs[i][index] * (h ** i)

    return y


def print_spline_funct(table, x, start, end):
    x_values = [i.get_x() for i in table]
    y_values = [i.get_y() for i in table]

    index = find_index(x_values, x)
    coeffs = calculate_coefs_spline(x_values, y_values, start, end)

    # print("x = {:.6g}".format(x))

    fx = coeffs[0][index]
    for i in range(1, len(coeffs)):
        fx += coeffs[i][index] * (x - x_values[index]) ** i

    print("F(x) = {:.6f}".format(fx), end=' ')

    # y = count_polynom(x, x_values, index, coeffs)
    # print("= {:.6f}".format(y))


def spline(table, x, start, end):
    x_values = [i.get_x() for i in table]
    y_values = [i.get_y() for i in table]

    coeffs = calculate_coefs_spline(x_values, y_values, start, end)

    index = find_index(x_values, x)

    y = count_polynom(x, x_values, index, coeffs)

    return y
