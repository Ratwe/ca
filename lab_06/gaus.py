def solve_ls_by_gaus_method(matrix):
    n = len(matrix)

    for i in range(n):
        maxEl = abs(matrix[i][i])
        maxRow = i

        for k in range(i + 1, n):
            if abs(matrix[k][i]) > maxEl:
                maxEl = abs(matrix[k][i])
                maxRow = k

        for k in range(i, n + 1):
            tmp = matrix[maxRow][k]
            matrix[maxRow][k] = matrix[i][k]
            matrix[i][k] = tmp

        for k in range(i + 1, n):
            c = - matrix[k][i] / matrix[i][i]
            for j in range(i, n + 1):
                if i == j:
                    matrix[k][j] = 0
                else:
                    matrix[k][j] += c * matrix[i][j]

    result = [0.0 for _ in range(n)]

    for i in range(n - 1, -1, -1):
        result[i] = matrix[i][-1]

        for j in range(i + 1, n):
            result[i] -= matrix[i][j] * result[j]

        result[i] /= matrix[i][i]

    return result

def simpson_integrate(a, b, function, x1, n) -> float:
    N = 2 * n
    x = (b - a)

    steps = [x / N * i for i in range(N + 1)]

    h = x / N

    s1 = 2 * sum([function(x1, steps[2 * j]) for j in range(1, N // 2)])
    s2 = 4 * sum([function(x1, steps[2 * j - 1]) for j in range(1, N // 2 + 1)])

    return h / 3 * (function(x1, steps[0]) + s1 + s2 + function(x1, steps[N]))

def Pn(n, value):
    if n == 0:
        return 1
    elif n == 1:
        return value

    return  1 / n * ((2 * n - 1) * Pn(n - 1, value) * value -
                     (n - 1) * Pn(n - 2, value))

def Pn_roots_search(n, real_left, real_right, epsilon):
    right = 1

    roots = []

    if n % 2 != 0:
        roots.append(0)

    goal_root_count = n // 2
    step = 0
    step_count = 1
    list_of_root_start = []

    while len(list_of_root_start) != goal_root_count:
        step_count *= 2
        step = 1 / step_count
        left = 0

        if n % 2 != 0:
            left += step

        list_of_root_start = []

        while left < right:
            if Pn(n, left) * Pn(n, left + step) <= 0:
                list_of_root_start.append(left)

            left += step

    buffer_roots = []

    for left in list_of_root_start:
        right = left + step

        MidX = (left + right) / 2

        while (right - left) / MidX > epsilon:
            if Pn(n, right) * Pn(n, MidX) > 0:
                left = right
                right = MidX
            else:
                right = left
                left = MidX

            MidX = (right + left) / 2

        buffer_roots.append(MidX)

        left += step

    roots += buffer_roots
    roots = [ -value for value in buffer_roots] + roots
    roots.sort()

    return roots

def integral_by_gauss(ax, bx, nx, ny, function, start_function, end_function, epsilon):
    roots = Pn_roots_search(nx, ax, bx, epsilon)

    matrix = [[roots[j] ** i for j in range(nx)] for i in range(nx)]

    for i in range(nx):
        matrix[i].append((1 - (-1) ** (i + 1)) / (i + 1))

    A = solve_ls_by_gaus_method(matrix)

    for i in range(len(roots)):
        roots[i] = (bx - ax) / 2 * roots[i] + (bx + ax) / 2

    return  (bx - ax) / 2 * sum([A[i] * simpson_integrate(start_function(roots[i]),
                                                          end_function(roots[i]),
                                                          function,
                                                          roots[i],
                                                          ny) for i in range(nx)])


