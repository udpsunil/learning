# sequence iteration
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
