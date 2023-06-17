import math
import numpy as np


def integrand(t):
    return math.exp(- (t ** 2) / 2)


def trapezoidal_rule(f, x, n=100):
    xa, xb = 0, x
    h = (xb - xa) / n
    sum = 0.5 * (f(xa) + f(xb))
    for i in range(1, n):
        x = xa + i * h
        sum += f(x)
    return h * sum


def f(x):
    integral = trapezoidal_rule(integrand, x)
    return (2 / math.sqrt(2 * math.pi)) * integral


def df(x):
    return 2 / math.sqrt(2 * math.pi) * math.exp(-(x ** 2) / 2)

    

def newton(c):
    steps = 1000
    x = 0.5
    eps = 1e-8

    i = 0
    while i < steps:
        fx = f(x) - c
        if abs(fx) < eps:
            return x

        dfx = df(x)
        if dfx == 0:
            return x
        x -= fx / dfx
    return None


print(newton(0.4608))
