# Ищем индекс ближайшего к Х значения в таблице
def get_index(table, x):
    diff = abs(table[0].x - x)
    index = 0

    for i in range(len(table)):
        if abs(table[i].x - x) < diff:
            diff = abs(table[i].x - x)
            index = i

    return index


# Какие точки будем использовать для аппроксимации
def get_bordered_table(table, index, n):
    left = index
    right = index

    # при чётном - опускаем границу
    # при нечётном - поднимаем
    for i in range(n - 1):
        if i % 2:
            if left == 0:
                right += 1
            else:
                left -= 1
        else:
            if right == len(table) - 1:
                left -= 1
            else:
                right += 1

    return table[left:right + 1]