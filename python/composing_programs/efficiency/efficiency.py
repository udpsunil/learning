def count_frames(f):
    def counted(*args):
        counted.open_count += 1
        counted.max_count = max(counted.max_count, counted.open_count)
        result = f(*args)
        counted.open_count -= 1
        return result
    counted.open_count = 0
    counted.max_count = 0
    return counted


def count(f):
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted


def fib(n):
    """Fibonacci sequence

    :param n: [description]
    :type n: [type]
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-2) + fib(n-1)


# Memoization
def memo(f):
    cache = {}

    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized