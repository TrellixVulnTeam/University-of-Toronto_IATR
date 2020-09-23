""" recursion exercises with nested lists
"""


import python_ta


def gather_lists(list_):
    """
    Return the concatenation of the sublists of list_.

    @param list[list] list_: list of sublists
    @rtype: list

    >>> list_ = [[1, 2], [3, 4]]
    >>> gather_lists(list_)
    [1, 2, 3, 4]
    """
    # special form of sum for "adding" lists
    return sum(list_, [])


def list_all(obj):
    """
    Return a list of all non-list elements in obj or obj's sublists, if obj
    is a list.  Otherwise, return a list containing obj.

    @param list|object obj: object to list
    @rtype: list

    >>> obj = 17
    >>> list_all(obj)
    [17]
    >>> obj = [1, 2, 3, 4]
    >>> list_all(obj)
    [1, 2, 3, 4]
    >>> obj = [[1, 2, [3, 4], 5], 6]
    >>> all([x in list_all(obj) for x in [1, 2, 3, 4, 5, 6]])
    True
    >>> all ([x in [1, 2, 3, 4, 5, 6] for x in list_all(obj)])
    True
    """
    if not isinstance(obj, list):
        return [obj]

    elif obj == []:
        return []

    else:
        return gather_lists([list_all(item) for item in obj])




def max_length(obj):
    """
    Return the maximum length of obj or any of its sublists, if obj is a list.
    otherwise return 0.

    @param object|list obj: object to return length of
    @rtype: int

    >>> max_length(17)
    0
    >>> max_length([1, 2, 3, 17])
    4
    >>> max_length([[1, 2, 3, 3], 4, [4, 5]])
    4
    """
    if not isinstance(obj, list):
        return 0
    elif all([not isinstance(item, list) for item in obj]):
        return len(obj)

    else:
        return max(max([max_length(item) for item in obj]), len(obj))
    #return max([len(obj)] + [max_length(item) if isinstance(item, list) else 0 for item in obj])arity



def list_over(obj, n):
    """
    Return a list of strings of length greater than n in obj,
    or sublists of obj, if obj is a list.
    If obj is a string of length greater than n, return a list
    containing obj.  Otherwise return an empty list.

    @param str|list obj: possibly nested list of strings, or string
    @param int n: non-negative integer
    @rtype: list[str]

    >>> list_over("five", 3)
    ['five']
    >>> list_over("five", 4)
    []
    >>> list_over(["one", "two", "three", "four"], 3)
    ['three', 'four']
    """
    if obj == []:
        return []

    elif not isinstance(obj, list):
        if len(obj) > n:
            return [obj]
        else:
            return []
    else:
        return gather_lists([list_over(item, n) for item in obj])



def list_even(obj):
    """
    Return a list of all even integers in obj,
    or sublists of obj, if obj is a list.  If obj is an even
    integer, return a list containing obj.  Otherwise return
    en empty list.

    @param int|list obj: possibly nested list of ints, or int
    @rtype: list[int]

    >>> list_even(3)
    []
    >>> list_even(16)
    [16]
    >>> list_even([1, 2, 3, 4, 5])
    [2, 4]
    >>> list_even([1, 2, [3, 4], 5])
    [2, 4]
    >>> list_even([1, [2, [3, 4]], 5])
    [2, 4]
    """
    if obj == []:
        return []

    elif not isinstance(obj, list):
        if obj % 2 == 0:
            return [obj]
        else:
            return []
    else:
        return gather_lists([list_even(item) for item in obj])


def count_even(obj):
    """
    Return the number of even numbers in obj or sublists of obj
    if obj is a list.  Otherwise, if obj is a number, return 1
    if it is an even number and 0 if it is an odd number.

    @param int|list obj: object to count even numbers from
    @rtype: int

    >>> count_even(3)
    0
    >>> count_even(16)
    1
    >>> count_even([1, 2, [3, 4], 5])
    2
    """
    if not isinstance(obj, list):
        if obj % 2 == 0:
            return 1
        else:
            return 0
    elif obj == []:
        return 0
    else:
        return sum([count_even(item) for item in obj])


def count_all(obj):
    """
    Return the number of elements in obj or sublists of obj if obj is a list.
    Otherwise, if obj is a non-list return 1.

    @param object|list obj: object to count
    @rtype: int

    >>> count_all(17)
    1
    >>> count_all([17, 17, 5])
    3
    >>> count_all([17, [17, 5], 3])
    4
    """
    if not isinstance(obj, list):
        return 1
    elif obj == []:
        return 0
    else:
        return sum([count_all(item) for item in obj])


def count_above(obj, n):
    """
    Return tally of numbers in obj, and sublists of obj, that are over n, if
    obj is a list.  Otherwise, if obj is a number over n, return 1.  Otherwise
    return 0.

    >>> count_above(17, 19)
    0
    >>> count_above(19, 17)
    1
    >>> count_above([17, 18, 19, 20], 18)
    2
    >>> count_above([17, 18, [19, 20]], 18)
    2
    """
    if not isinstance(obj, list):
        if obj > n:
            return 1
        else:
            return 0

    elif obj == []:
        return 0

    else:
        return sum([count_above(item, n) for item in obj])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    python_ta.check_all()
