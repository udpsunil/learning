# Function that returns a function as a value

def make_adder(n):
    """Return a function that takes one argument K and returns K + N

    Args:
        n ([type]): [description]
    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder
