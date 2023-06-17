def divided_diff(table):
    temp = [[0] * (len(table)) for i in range(len(table) + 2)]

    for i in range(len(table)):
        temp[0][i] = table[i][0]
        temp[1][i] = table[i][2]
        temp[2][i] = table[i][1]

    x_barier = 1

    for i in range(3, len(temp)):
        for j in range(len(temp[0]) - i + 2):
            if temp[0][j] - temp[0][j + x_barier] == 0:
                temp[i][j] = temp[1][j]
            else:
                temp[i][j] = (temp[i - 1][j] - temp[i - 1][j + 1]) / (temp[0][j] - temp[0][j + x_barier])
        x_barier += 1

    return [temp[i][0] for i in range(3, len(temp))]


def select_points_newton(table, x, n):
    new_table = []

    pos = 0
    while pos < len(table) - 1 and table[pos][0] < x:
        pos += 1

    # if pos != 0 and abs(table[pos][0] - x) > abs(table[pos - 1][0] - x):
    #     pos -= 1

    new_table.append(table[pos].copy())

    l_bound = pos - 1
    r_bound = pos + 1

    while len(new_table) < n + 1:
        if l_bound >= 0 and len(new_table) < n + 1:
            new_table.append(table[l_bound].copy())
            l_bound -= 1
        if r_bound < len(table) and len(new_table) < n + 1:
            new_table.append(table[r_bound].copy())
            r_bound += 1

    new_table.sort(key=lambda x: x[0])

    if len(new_table) == n + 1:
        return new_table
    else:
        return None


def approximate_newton(table, x, n):
    selected_points = select_points_newton(table, x, n)

    diffs = divided_diff(selected_points)

    res = selected_points[0][1]

    accum = 1
    i = 0
    while i < len(diffs):
        accum *= (x - selected_points[i][0])
        res += accum * diffs[i]
        i += 1

    return res
