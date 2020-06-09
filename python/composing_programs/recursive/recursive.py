
def split(n):
    """Split all digits into last digit and rest of the digits

    Args:
        n ([type]): [description]

    Returns:
        [type]: [description]
    >>> split(2013)
    (201, 3)
    """
    return n // 10, n % 10


def sum_digits(n):
    """Return the sum of the digits of positive integer n

    Args:
        n ([type]): [description]
    >>> sum_digits(12345)
    15
    """
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last
