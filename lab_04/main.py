import math

from readTableFunction import readFileTable, printTable_1D, printTable_2D, \
    inputApproximateDegree, changeWeigth, changeAllWeigth
from generateTableFunction import generateTable_1D, \
    generateTable_2D
from approximation import leastSquaresMethod_1D, drawGraficBy_AproxFunction_1D, \
    leastSquaresMethod_2D, drawGraficBy_AproxFunction_2D

from printAboutTheory import printFunction_1D, printSlau_1D, printAboutSlauCoefficients_1D

from differentialEquation import solveDiffEq

import numpy as np
from pointClass import *
from matplotlib import pyplot as plt
from math import exp, sin, sqrt


def f_1d(x):
    return x * math.e**x


def f_2d(x, y):
    return x ** 2 + y ** 2

    # однополосный гипербалоид
    # a = 2
    # b = 3
    # c = 5
    # return sqrt((x**2 / a**2 + y**2 / b**2 - 1) / c**2)

    # двуполосный гипербалоид
    # a = 2
    # b = 3
    # c = 5
    # return sqrt((x**2 / a**2 + y**2 / b**2 + 1) / c**2)

    # эллиптический параболоид
    # a = 2
    # b = 3
    # return x**2 / a**2 + y**2 / b**2

    # гипербoлический параболоид
    # a = 2
    # b = 3
    # return x**2 / a**2 - y**2 / b**2


menu = "\n Меню \n" \
       "1  - Прочитать файл\n" \
       "2  - Cгенерировать таблицу для одномерной аппроксимации\n" \
       "3  - Cгенерировать таблицу для двумерной аппроксимации\n" \
       "4  - Вывести таблицу\n" \
       "5  - Изменить вес точки\n" \
       "6  - Задать вес всех точек равным 1\n" \
       "7  - Решить и построить график\n" \
       "8  - Решение обыкновенного дифференциального уравнения: y'' + xy' + y = 2x (y(0)=1, y(1)=0) \n" \
       "0  - Выход\n"

step = -1
mode = -1
table = list()

while step != 0:
    print(menu)
    step = int(input("Ввести пункт: "))
    if step == 2:
        mode = 1
        xs = float(input("Введите X начальное: "))
        xe = float(input("Введите X конечное: "))
        amount = int(input("Введите кол-во точек: "))
        table = generateTable_1D(f_1d, xs, xe, amount)
    elif step == 3:
        mode = 2
        xs = float(input("Введите X начальное: "))
        xe = float(input("Введите X конечное: "))
        amountX = int(input("Введите кол-во точек X: "))
        ys = float(input("Введите Y начальное: "))
        ye = float(input("Введите Y конечное: "))
        amountY = int(input("Введите кол-во точек Y: "))
        table = generateTable_2D(f_2d, xs, xe, ys, ye, amountX, amountY)
    elif step == 4:
        if mode == -1:
            print("Данные не прочитаны!")
        elif mode == 1:
            printTable_1D(table)
        elif mode == 2:
            printTable_2D(table)
    elif step == 5:
        if mode == -1:
            print("Данные не прочитаны!")
        else:
            changeWeigth(table)
    elif step == 6:
        if mode == -1:
            print("Данные не прочитаны!")
        else:
            changeAllWeigth(table)
    elif step == 7:
        if mode == -1:
            print("Данные не прочитаны!")
        else:
            n = inputApproximateDegree()
            if mode == 1:
                printSlau_1D(n)
                printAboutSlauCoefficients_1D()
                print(table)
                fn = leastSquaresMethod_1D(table, n)
                drawGraficBy_AproxFunction_1D(fn, table)
            elif mode == 2:
                x = float(input("Ввести x: "))
                y = float(input("Ввести y: "))
                fn = leastSquaresMethod_2D(table, n)
                print("Результат f({:.6g}, {:.6g}) =".format(x, y), fn(x, y))
                drawGraficBy_AproxFunction_2D(fn, table, n)
    elif step == 8:
        solveDiffEq()
