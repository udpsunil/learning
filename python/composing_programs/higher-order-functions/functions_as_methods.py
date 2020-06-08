def square_root(a):
    x = 1
    while x * x != a:
        print(x)
        x = square_root_update(x, a)
    return x


def square_root_update(x, a):
    return (x + a / x) / 2


def cube_root_update(x, a):
    return (2 * x + a / (x * x)) / 3


def improve(update, close, guess=1):
    seen = []
    while not close(guess) and guess not in seen:
        seen.append(guess)
        guess = update(guess)
    print(seen)
    return guess


def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance


def square_root(a):
    def update(x):
        return square_root_update(x, a)

    def close(x):
        return approx_eq(x * x, a)

    return improve(update, close)


def cube_root(a):
    return improve(
        lambda x: cube_root_update(x, a),
        lambda x: approx_eq(x * x * x, a)
    )


def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)
    return update


def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)


def square_root_newton(a):
    def f(x):
        return x * x - a

    def df(x):
        return 2 * x

    return find_zero(f, df)


def power(x, n):
    product, k = 1, 0
    while k < n:
        product, k = product * x, k + 1
    return product


def nth_root_of_a(n, a):
    def f(x):
        return power(x, n) - a

    def df(x):
        return n * power(x, n - 1)
    return find_zero(f, df)
