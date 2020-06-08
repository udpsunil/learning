def square_root(a):
    x = 1
    while x * x != a:
        print(x)
        x = square_root_update(x, a)
    return x


def square_root_update(x, a):
    return (x + a / x) / 2


def cube_root(a):
    x = 1
    while x * x * x != a:
        x = cube_root_update(x, a)
    return x


def cube_root_update(x, a):
    return (2 * x + a / (x * x)) / 3
