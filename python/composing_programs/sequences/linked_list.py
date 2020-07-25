empty = 'empty'


def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair

    Args:
        s ([type]): [description]
    """
    return s == empty or (len(s) == 2 and is_link(s[1]))


def link(first, rest):
    """Construct a linked list from its first and reset of elements

    Args:
        first ([type]): [description]
        rest ([type]): [description]
    """
    assert is_link(rest), "rest must be a linked list"
    return [first, rest]


def first(s):
    """Return the first element of a linked list s

    Args:
        s ([type]): [description]
    """
    assert is_link(s), "first only applies to linked lists"
    assert s != empty, "empty linked list has no first element"
    return s[0]


def rest(s):
    """Return the rest of the elements of a linked list s.

    Args:
        s ([type]): [description]
    """
    assert is_link(s), "rest only applies to linked lists"
    assert s != empty, "empty linked list has no rest"
    return s[1]


def len_link(s):
    """Return the length of linked list s

    Args:
        s ([type]): [description]
    """
    length = 0
    while s != empty:
        s, length = rest(s), length+1
    return length


def getitem_link(s, i):
    """Return the element at index i of linked list s.

    Args:
        s ([type]): [description]
        i ([type]): [description]
    """
    while i > 0:
        s, i = rest(s), i-1
    return first(s)


def len_link_recursive(s):
    """Return the length of a linked list s."""
    if s == empty:
        return 0
    return 1 + len_link_recursive(rest(s))


def getitem_link_recursive(s, i):
    """Return the element at index i of linked list s"""
    if i == 0:
        return first(s)
    return getitem_link_recursive(rest(s), i-1)

def extend_link(s, t):
    """Return a list with the elements of s followed by those of t.

    Args:
        s ([type]): [description]
        t ([type]): [description]
    """
    assert is_link(s) and is_link(t)
    if s == empty:
        return t
    else:
        return link(first(s), extend_link(rest(s), t))