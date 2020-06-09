# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from math import gcd


def rational(n, d):
    g = gcd(n, d)
    return [n//g, d//g]


def numer(x):
    return x[0]


def denom(x):
    return x[1]


def add_rational(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)


def mul_rational(x, y):
    return rational(numer(x) * numer(y), denom(x) * denom(y))


def print_rational(x):
    print(numer(x), '/', denom(x))


def reationals_are_equal(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)
