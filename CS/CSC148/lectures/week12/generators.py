"""experiment with generators
"""


def myrange_using_list(target):
    """ Generate items in range of [0,target-1] and build a list
    """
    num, num_list = 0, []
    while num < target:
        num_list.append(num)
        num += 1
    return num_list


class MyRange:
    """ range implemented using generator pattern.
    """
    def __init__(self, target):
        self.target = target
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < self.target:
            current, self.num = self.num, self.num+1
            return current
        else:
            raise StopIteration()


def myrange_using_generator(target):
    """ our own range generator that yields items
    """
    num = 0
    while num < target:
        yield num
        num += 1


def find_any_true(contents):
    """ Find if at least one of the items in contents is true.
    """
    if any(contents):
        print("at least 1 true")
    else:
        print("none true")


def find_exactly_one_true(contents):
    """ Find if exactly one of the items in contents is true.
    """
    if any(contents):
        # continues from where the previous any() left off!
        if not any(contents):
            print("exactly 1 true")
        else:
            print("more than 1 true")
    else:
        print("none true")


if __name__ == '__main__':

    # lst = [i == 5 for i in range(10)]
    # Find if any element is True in this list
    # find_any_true(lst)

    # Now let's see if exactly one is true in the list
    # This is normally what we could do:
    # count = sum([1 for i in lst if i is True])
    # if count == 1:
    #     print("exactly 1 true")
    # elif count > 1:
    #     print("more than 1 true")
    # else:
    #     print("none true")
    gen = MyRange(10)
    print(4 in gen)
    print(3 in gen)
    #gen = (i > 5 for i in range(10))
    # Find if any elements are true
    # gen.__next__() produces next element on demand.
    # find_any_true(gen)

    # Find if exactly one element is True in this generator.
    # Use the generator abilities in a really nice way.
    # Trace it with the debugger to convince yourselves.
    # Just make sure you don't uncomment the previous
    # call to find_any_true, which would otherwise "consume"
    # some of the generator
    #find_exactly_one_true(gen)

    # This won't work for a list as you expect it does for a generator.
    # As usual, trace the code to figure out what happens
    # find_exactly_one_true(lst)
    #
    # # Create our own ranges, using a list ..
    # sum_range = sum(myrange_using_list(1000))
    # print(sum_range)
    #
    # # .. our own range, by rolling our own generator
    # sum_range = sum(MyRange(1000))
    # print(sum_range)
    #
    # # .. again with a generator, this time using "yield"
    # sum_range = sum(myrange_using_generator(1000))
    # print(sum_range)


