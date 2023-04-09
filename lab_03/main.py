import matplotlib.pyplot as plt
import numpy as np

from spline import *
from newton import *


def read_table(name):
    data = [] # массив матриц для хранения таблиц 5 * 5 * 5  
    with open(name, mode='r') as f:
        n, m = map(int, f.readline().split())
        for _ in range(n):
            temp = []
            for _ in range(m):
                temp.append(list(map(int, f.readline().split())))
            data.append(temp)
   
    return data


def get_value_for_3d_newton(table, x, y, nx, ny):
    new_table = [[px] for px in range(len(table))]
    for j in range(len(table)):
        temp = [[i, table[j][i], 1] for i in range(len(table[0]))] # матрица фиксируем одну строку [[0, num, 1 ] ... [i, num, 1 ]]
        new_table[j] += [approximate_newton(temp, y, ny), 1] # находим значение в точке Y 

    
    # print('{:20}{:20}'.format('x', 'y'))
    # print('----------------------------------------')
    # for line in new_table:
    #     print("{:<20.3f}{:<20.3f}".format(line[0], line[1]))
    # print('----------------------------------------')
    
    return approximate_newton(new_table, x, nx)


def get_value_for_3d_spline(table, x, y):
    new_table = [[px] for px in range(len(table))]
    for j in range(len(table)):
        temp = [[i, table[j][i]] for i in range(len(table[0]))]
        spline = Spline(temp, 0, 0)
        new_table[j].append(spline.aproximate_value(y))
    
    spline = Spline(new_table, 0, 0)
    return spline.aproximate_value(x)


def get_value_for_3d_mashup_nx(table, x, y, nx):
    new_table = [[px] for px in range(len(table))]
    for j in range(len(table)):
        temp = [[i, table[j][i]] for i in range(len(table[0]))]
        spline = Spline(temp, 0, 0)
        new_table[j]+= [spline.aproximate_value(y), 1]
    
    return approximate_newton(new_table, x, nx)


def get_value_for_3d_mashup_ny(table, x, y, ny):
    new_table = [[px] for px in range(len(table))]
    for j in range(len(table)):
        temp = [[i, table[j][i], 1] for i in range(len(table[0]))]
        new_table[j] += [approximate_newton(temp, y, ny), 1]
    
    spline = Spline(new_table, 0, 0)
    return spline.aproximate_value(x)


def get_value_for_4d_newton(table, x, y, z, nx, ny, nz):
    
    new_table = [[px] for px in range(len(table))]
    print(new_table)
    for i in range(len(table)):
        new_table[i] += [get_value_for_3d_newton(table[i], x, y, nx, ny), 1] # фиксируем zi  и считаем для 3 мерного 2 переменных
    
    # print('{:20}{:20}'.format('z', 'u'))
    # print('----------------------------------------')
    # for line in new_table:
    #     print("{:<20.3f}{:<20.3f}".format(line[0], line[1]))
    # print('----------------------------------------')    
    
    return approximate_newton(new_table, z, nz)


def get_value_for_4d_spline(table, x, y, z):
    new_table = [[px] for px in range(len(table))]
    for i in range(len(table)):
        new_table[i].append(get_value_for_3d_spline(table[i], x, y)) 
    
    spline = Spline(new_table, 0, 0)
    
    return spline.aproximate_value(z)


def get_value_for_4d_mashup_nx(table, x, y, z, nx):
    new_table = [[px] for px in range(len(table))]
    for i in range(len(table)):
        new_table[i].append(get_value_for_3d_mashup_nx(table[i], x, y, nx)) 

    spline = Spline(new_table, 0, 0)
    
    return spline.aproximate_value(z) 


def get_value_for_4d_mashup_ny(table, x, y, z, ny):
    new_table = [[px] for px in range(len(table))]
    for i in range(len(table)):
        new_table[i].append(get_value_for_3d_mashup_ny(table[i], x, y, ny)) 

    spline = Spline(new_table, 0, 0)
    
    return spline.aproximate_value(z) 

def get_value_for_4d_mashup_nz(table, x, y, z, nz):
    new_table = [[px] for px in range(len(table))]
    for i in range(len(table)):
        new_table[i] += [get_value_for_3d_spline(table[i], x, y), 1] 

    return approximate_newton(new_table, z, nz)

def get_value_for_4d_mashup_nx_ny(table, x, y, z, nx, ny):
    new_table = [[px] for px in range(len(table))]
    for i in range(len(table)):
        new_table[i] += [get_value_for_3d_newton(table[i], x, y, nx, ny), 1] 
    
    spline = Spline(new_table, 0, 0)
    
    return spline.aproximate_value(z)

def get_value_for_4d_mashup_nx_nz(table, x, y, z, nx, nz):
    new_table = [[px] for px in range(len(table))]
    for i in range(len(table)):
        new_table[i] += [get_value_for_3d_mashup_nx(table[i], x, y, nx), 1] 
    
    return approximate_newton(new_table, z, nz)


def get_value_for_4d_mashup_ny_nz(table, x, y, z, ny, nz):
    new_table = [[px] for px in range(len(table))]
    for i in range(len(table)):
        new_table[i] += [get_value_for_3d_mashup_ny(table[i], x, y, ny), 1] 
    
    return approximate_newton(new_table, z, nz)


def main():
    data = read_table('./data.txt')
    x = float(input('Введите x: '))
    y = float(input('Введите y: '))
    z = float(input('Введите z: '))
    nx = int(input('Введите nx: '))
    ny = int(input('Введите ny: '))
    nz = int(input('Введите nz: '))
    
    print("Интерполяция Полиномом Ньютона: {:.3f}".format(get_value_for_4d_newton(data, x, y, z, nx, ny, nz)))
    print("Интерполяция Сплайном (0, 0): {:.3f}".format(get_value_for_4d_spline(data, x, y, z)))
    print("Интерполяция смешанная (по x полином): {:.3f}"\
        .format(get_value_for_4d_mashup_nx(data, x, y, z, nx)))
    print("Интерполяция смешанная (по y полином): {:.3f}"\
        .format(get_value_for_4d_mashup_ny(data, x, y, z, ny)))
    print("Интерполяция смешанная (по z полином): {:.3f}"\
        .format(get_value_for_4d_mashup_nz(data, x, y, z, nz)))
    print("Интерполяция смешанная (по x и y полином): {:.3f}"\
        .format(get_value_for_4d_mashup_nx_ny(data, x, y, z, nx, ny)))
    print("Интерполяция смешанная (по x и z полином): {:.3f}"\
        .format(get_value_for_4d_mashup_nx_nz(data, x, y, z, nx, nz)))
    print("Интерполяция смешанная (по y и z полином): {:.3f}"\
        .format(get_value_for_4d_mashup_ny_nz(data, x, y, z, ny, nz)))
    
if __name__ == '__main__':
    main()
    
