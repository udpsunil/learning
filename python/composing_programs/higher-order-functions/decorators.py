def trace(fn):
    """Returns a version of function that first prints a message before function is called.

    Args:
        fn (function): [description]
    """
    def traced(x):
        print('Calling ', fn, 'on argument ', str(x))
        return fn(x)
    return traced


@trace
def square(x):
    return x * x


@trace
def sum_squares_up_to(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + square(k), k + 1
    return total
