def depth(obj):
    """

    """
    if obj == []:
        return 1
    elif isinstance(obj, list):
        return 1 + max([depth(x) for x in obj])

    else:
        return 0


def nested_contains(L, value):
    """

    """
    return True in [nested_contains(x, value) if isinstance(x, list) else x == value for x in L]
           #any([nested_contains(x, value) if isinstance(x, list) else x == value for x in L])

if __name__ == '__main__':
    L = ['how', ['now', 'low'],1]
    print(nested_contains(L, 'low'))

