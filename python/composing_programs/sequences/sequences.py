# sequence iteration
from operator import mul, add

digits = [1, 8, 2, 8]


def count(s, value):
    """Count the number of occurences of value in sequence s.

    Args:
        s ([type]): [description]
        value ([type]): [description]
    >>> count(digits, 8)
    2
    """
    total, index = 0, 0
    while index < len(s):
        if s[index] == value:
            total += 1
        index += 1
    return total


def divisors(n):
    """Return list of divisors of a given number n

    Args:
        n ([type]): [description]

    Returns:
        [type]: [description]
    >>> divisors(4)
    [1, 2]
    >>> divisors(12)
    [1, 2, 3, 4, 6]
    """
    return [1] + [x for x in range(2, n) if n % x == 0]


def apply_to_all(map_fn, s):
    return [map_fn(x) for x in s]


def keep_if(filter_fn, s):
    return [x for x in s if filter_fn(x)]


def reduce_to(reduce_fn, s, initial):
    """[summary]

    Args:
        reduce_fn ([type]): [description]
        s ([type]): [description]
        initial ([type]): [description]

    Returns:
        [type]: [description]
    >>> reduce_to(mul, [2,4,8], 1)
    64
    """
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced


def divisors_of(n):
    """[summary]

    Args:
        n ([type]): [description]

    Returns:
        [type]: [description]
    >>> divisors_of(12)
    [1, 2, 3, 4, 6]
    """
    def divides_n(x): return n % x == 0
    return [1] + keep_if(divides_n, range(2, n))


def sum_of_divisors(n):
    return reduce_to(add, divisors_of(n), 0)


def perfect(n):
    return sum_of_divisors(n) == n


print(keep_if(perfect, range(1, 1000)))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
