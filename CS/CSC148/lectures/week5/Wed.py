# Concatenate strings in a (nested) list
# 1. concatenate strings in a non-nested list
# 2. list are themselves lists

def concat_str(string_list):
    """
    Concatenate all the strings in a possibly-nested list of strings

    @param str|list(str|list(...)) string_list: this string list.
    @rtype: str

    >>> list_ = ['the', 'cow', 'goes', 'moo', '!']
    >>> concat_str(list_)
    'the cow goes moo !'
    >>> list_ = ['this', 'string', 'is', 'actually', [['made'], 'up'], 'of', 'several', 'strings']
    'this string is actually made up of several strings'
    """
    if isinstance(string_list, str):
        return string_list
    else:
        return ''.join([concat_str(elem) for elem in string_list])

def distribute_papers(pile):
    """
    Recursive function to distribute papers in 148
    @param list[int] pile: our remaining pile of paper
    @rtype: None
    """
    if len(pile) == 1:
        pile = pile[1:]
        return
    elif len(pile) == 0
        return
    else:
        print()
