""" re--implement each function below in ex4.py
*without*  using comprehensions, filter, zip, sum
or max.
"""


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
    # sum of products of pairs of corresponding coordinates of u and v
    return sum([u_coord * v_coord for u_coord, v_coord in zip(u, v)])


def matrix_vector_prod(m, u):
    """
    Return the matrix-vector product of m x u

    @param list[list[float]] m: matrix
    @param list[float] u: vector
    @rtype: list[float]
    >>> matrix_vector_prod([[1.0, 2.0], [3.0, 4.0]], [5.0, 6.0])
    [17.0, 39.0]
    """
    return [dot_prod(v, u) for v in m]


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
    def _ascending_pythagorean(t):
        # """
        # Return whether t is pythagorean and non-descending.
        #
        # @param tuple[int] t: triple of integers to check
        # """
        return (t[0] <= t[1] <= t[2]) and (t[0]**2 + t[1]**2) == t[2]**2

    # filter just the ones that satisfy ascending_pythagorean
    # produce a list from the filter for ascending_pythagoreans from...
    return list(filter(_ascending_pythagorean,
                       # ...list of all triples in the range 1..n
                       [(i, j, k)
                        for i in range(1, n + 1)
                        for j in range(1, n + 1)
                        for k in range(1, n + 1)]))


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
        return max(len(obj), max([max_length(x) for x in obj]))
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
        return sum([count_even(x) for x in obj])


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
        return sum([count_above(x, n) for x in obj])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
