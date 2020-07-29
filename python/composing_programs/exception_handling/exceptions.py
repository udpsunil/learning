def invert(x):
    result = 1 / x  # Raise a ZeroDivisionError if x is 0
    print('Never printed if x is 0')
    return result


def invert_safe(x):
    try:
        return invert(x)
    except ZeroDivisionError as e:
        return str(e)

