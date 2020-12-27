def count_lists(L):
    '''(list or non-list) -> int

    Return 0 if L is a non-list, or number of lists in possibly-nested L.

    >>> count_lists([2, 1, 3])
    1
    >>> count_lists([2, 1, 3, '[4]'])
    1
    >>> count_lists([7, [2, 1, 3], 9, [3, 2, 4]])
    3
    >>> count_lists([7, [2, 1, [3, 4], 5], 9, [3, 2, 4]])
    4
    '''
    if isinstance(L, list):
        return 1 + sum([count_lists(x) for x in L])
    else: # L is not a list
        return 0

def count_all(L):
    '''(list or non-list) -> int

    Return 0 if L is a non-list, or number of lists, plus non-list elements,
    in possibly-nested L.

    >>> count_all([2, 1, 3])
    4
    >>> count_all([2, 1, 3, '[4]'])
    5
    >>> count_all([7, [2, 1, 3], 9, [3, 2, 4]])
    11
    >>> count_all([7, [2, 1, [3, 4], 5], 9, [3, 2, 4]])
    14
   '''
    if isinstance(L, list):
        return 1 + sum([count_all(x) for x in L])
    else: # L is not a list
        return 1

def nested_contains(L, v):
    '''(list or non-list, object) -> bool

    Return False if L is not a list, or whether L, or any list nested in L, 
    contains a value equivalent to v.

    >>> nested_contains([1, 2, 3], 2)
    True
    >>> nested_contains([1, [2, 3]], [2, 3])
    True
    >>> nested_contains([1, [2, 3]], 2)
    True
    >>> nested_contains([1, [2, 3]], 7)
    False
    >>> nested_contains([1, [2, 3]], [3, 2])
    False
    '''
    if isinstance(L, list):
        # any(L) returns True if L contains at least one non-False element
        return any([(x == v or nested_contains(x, v)) for x in L])
    else: # L is not a list
        return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()

