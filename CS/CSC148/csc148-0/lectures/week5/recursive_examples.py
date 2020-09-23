""" Some recursive functions on nested lists
"""


def depth(obj):
    """ Calculate the depth of a list object obj.
    Return 0 if obj is a non-list, or 1 + maximum
    depth of elements of obj, a possibly nested
    list of objects.

    Assume: obj has finite nesting depth

    @param int|list[int|list[...]] obj: possibly nested list of objects
    @rtype: int

    >>> depth(3)
    0
    >>> depth([])
    1
    >>> depth([1, 2, 3])
    1
    >>> depth([1, [2, 3], 4])
    2
    >>> depth([[], [[]]])
    3
    """
    if not isinstance(obj, list):
        # obj is not a list
        return 0
    elif obj == []:
        return 1
    else:
        # obj is a list
        return 1 + max([depth(elem) for elem in obj])


def rec_max(obj):
    """ Calculate the maximum in a list object obj.
    Return obj if it's an int, or the maximum int in obj,
    a possibly nested list of numbers.

    Assume: obj is an int or non-empty list with finite nesting depth,
    and obj doesn't contain any empty lists

    @param int|list[int|list[...]] obj: possibly nested list of int
    @rtype: int

    >>> rec_max([17, 21, 0])
    21
    >>> rec_max([17, [21, 24], 0])
    24
    >>> rec_max(31)
    31
    """
    if not isinstance(obj, list):
        # obj is not a list
        return obj
    elif obj == []:
        raise Exception("List should not be empty or contain empty sublists")
    else:
        # obj is a list
        return max([rec_max(elem) for elem in obj])


def concat_strings(string_list):
    """
    Concatenate all the strings in possibly-nested string_list.

    @param list[str]|str string_list: a list of strings
    @rtype: str

    >>> list_ = (["The", "cow", "goes", "moo", "!"])
    >>> concat_strings(list_)
    'The cow goes moo !'
    >>> list_ = (["This", "sentence", "is actually", \
                  "constructed", ["from", ["other"], "smaller"], "strings"])
    >>> concat_strings(list_)
    'This sentence is actually constructed from other smaller strings'
    """
    if isinstance(string_list, str):
        # string_list is a str
        return string_list
    else:
        return " ".join([concat_strings(elem) for elem in string_list])


def distribute_papers(pile):
    """ Recursive function to distribute papers to the class.

    Assume: pile is a list of papers, each represented by their unique
    paper number. Each student takes 1 paper, then distributes further
    two halves of their remaining pile to two other students who will
    do the exact same thing. When no more papers left or only 1 left,
    then the problem becomes trivial.

    @param list[int] pile: a pile of papers
    @rtype: None
    """
    if len(pile) == 0:
        # all done
        print("All done")
    elif len(pile) == 1:
        # all done
        print("My pile: {} => Taking paper {} for myself".format(pile, pile[0]))
        pile = pile[1:]
        print("All done")
    else:
        print("My pile: {} => Taking paper {} for myself".format(pile, pile[0]))
        pile = pile[1:]
        # 2 recursive calls on each half of the pile
        middle = len(pile) // 2
        distribute_papers(pile[0: middle])
        distribute_papers(pile[middle:])

def concat_strings(string_list):
    """
    Concatenate all the strings in possibly-nested string_list.

    @param list[str]|str string_list: string(s) to concatenate
    @rtype: str

    >>> list_ = 'cat'
    >>> concat_strings(list_)
    'cat'
    >>> list_ = ['cat', 'dog']
    >>> concat_strings(list_)
    'catdog'
    >>> list_ = ["how", ["now", "brown"], "cow"]
    >>> concat_strings(list_)
    'hownowbrowncow'
    """
    # if this isn't a list, ie. it's an innermost element, don't recurse
    if not isinstance(string_list, list):
        return string_list
    else:
        return ''.join([concat_strings(x) for x in string_list])


def nested_contains(L, value):
    """
    Return whether L, or any nested sub-list of list_ contains value.

    @param list L: list to search
    @param object value: non-list value to search for
    @rtype: bool

    >>> list_ = ["how", ["now", "brown"], 1]
    >>> nested_contains(list_, "brown")
    True
    >>> nested_contains([], 5)
    False
    >>> nested_contains([5], 5)
    True
    """

    # since nested_contains returns a bool
    # and the == evaluates to a bool
    # this is a list of bools
    return any([nested_contains(x, value)
                    if isinstance(x, list)
                    else x == value
                    for x in L])

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print(depth(21))
    print(depth([5]))
    print(depth([5, [3, 17, 1], [2, 4], 6]))
    print(depth([14, 7, [5, [3, 17, 1], [2, 4], 6], 9]))
    print(depth([]))
    print(depth(None))
    print()

    print(rec_max(21))
    print(rec_max([5, [3, 17, 1], [2, 4], 6]))
    print(rec_max([14, 7, [5, [3, 17, 1], [2, 4], 6], 9]))
    # print(rec_max([])) # ==> Will raise an exception, as it should
    print()

    L = [1, 2, 3]
    print(L)
    L.append(L)
    print("L    = ", L)
    print("L[3] = ", L[3])
    print(L is L[3])
    print("id(L):    ", id(L))
    print("id(L[3]): ", id(L[3]))
    print()

    L1 = [1, 2, 3]
    print(L1)
    L1.append(L1[:])
    print("L1    = ", L1)
    print("L1[3] = ", L1[3])
    print(L1 is L1[3])
    print("id(L1):    ", id(L1))
    print("id(L1[3]): ", id(L1[3]))

    print('Depth =', depth(L1))
    # print('Depth =', depth(L))  # ==> Infinite recursion

    print(concat_strings(["The", "cow", "goes", "moo", "!"]))
    print(concat_strings(["This", "sentence", "is actually",
                          "constructed", ["from", "other smaller"], "strings"]))
    print(concat_strings([]))  # ==> Has no strings, prints an empty line
    print(concat_strings(["Moo", []]))
    # print(concat_strings(None)) # ==> Pycharm warning: type contract not met
    print()

    distribute_papers([1, 2, 3, 4, 5, 6, 7])
    # distribute_papers([])
    # distribute_papers([1])
    # distribute_papers([1, 2, 3, 4])
