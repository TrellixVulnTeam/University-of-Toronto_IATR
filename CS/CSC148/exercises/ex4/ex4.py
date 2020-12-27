
def dot_prod(u, v):
    """
    Return the dot product of u and v

    @param list[float] u: vector of floats
    @param list[float] v: vector of floats
    @rtype: float

    >>> dot_prod([1.0, 2.0], [3.0, 4.0])
    11.0
    """
    assert len(u) == len(v)
    res = 0
    for i in range(len(u)):
        res += u[i] * v[i]
    return res


def matrix_vector_prod(m, u):
    """
    Return the matrix-vector product of m x u

    @param list[list[float]] m: matrix
    @param list[float] u: vector
    @rtype: list[float]
    >>> matrix_vector_prod([[1.0, 2.0], [3.0, 4.0]], [5.0, 6.0])
    [17.0, 39.0]
    """
    res = []
    for i in m:
        res.append(dot_prod(i, u))
    return res

def pythagorean_triples(n):
    """
    Return list of pythagorean triples as non-descending tuples
    of ints from 1 to n.

    Assume n is positive.

    @param int n: upper bound of pythagorean triples

    >>> pythagorean_triples(5)
    [(3, 4, 5)]
    """
    # helper to check whether a triple is pythagorean and non_descending
    # you could also use a lambda instead of this nested function def.
    res = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                if i <= j <= k and (i ** 2 + j ** 2) == k ** 2:
                    res.append((i, j, k))
    return res


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
    if obj == []:
        return 0
    elif isinstance(obj, list):
        res = 0
        for item in obj:
            if max_length(item) > res:
                res = max_length(item)
        if len(obj) > res:
            res = len(obj)
        return res
    else:
        return 0


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
    if isinstance(obj, int) and obj % 2 == 0:
        return 1
    elif isinstance(obj, int):
        return 0
    else:
        res = 0
        for x in obj:
            res += count_even(x)
        return res

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
    if isinstance(obj, int) and obj > n:
        return 1
    elif isinstance(obj, int):
        return 0
    else:
        res = 0
        for item in obj:
            res += count_above(item, n)
        return res

