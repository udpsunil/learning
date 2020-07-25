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


# Violation of abstractions defined earlier

def square_rational_no_violation(x):
    return mul_rational(x, x)


def square_rational_with_one_level_violation(x):
    return rational(numer(x) * numer(x), denom(x) * denom(x))


def square_rational_with_two_level_violation(x):
    return [x[0] * x[0], x[1] * x[1]]


#================================================#
# Implementing the same rational abstraction but with different programming constructs# 

def pair(x, y):
    """Return a function that represents a pair.

    Args:
        x ([type]): [description]
        y ([type]): [description]
    """
    def get(index):
        if index== 0:
            return x
        elif index == 1:
            return y
    return get

def select(p, i):
    """Return the element at index i of pair p

    Args:
        p ([type]): [description]
        i ([type]): [description]
    """
    p(i)
