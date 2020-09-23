""" Quick sort """


def qs(list_):
    """
    Return a new list consisting of the elements of list_ in
    ascending order.

    @param list list_: list of comparables
    @rtype: list

    >>> qs([1, 5, 3, 2])
    [1, 2, 3, 5]
    """
    if len(list_) < 2:
        return list_[:]  # list_ is sorted, so make a copy
    else:
        # return (everything smaller than pivot, sorted) + pivot
        # + (everything larger than pivot, sorted)
        pivot = list_[0]  # could choose any pivot
        smaller_than_pivot = [v for v in list_ if v < pivot]
        larger_than_pivot = [v for v in list_[1:] if v >= pivot]
        return qs(smaller_than_pivot) + [pivot] + qs(larger_than_pivot)
