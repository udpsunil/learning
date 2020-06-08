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
