from stack import Stack


def list_stack(lst, stack):
    for item in lst:
        stack.add(item)


    while not stack.is_empty():
        r1 = stack.remove()
        if isinstance(r1, list):
            for item in r1:
                stack.add(item)

        else:
            print(r1)






if __name__ == '__main__':
    s = Stack()
    text = input('Type a string:')
    s.add(text)

    while text != 'end':
        text = input('Type a string:')
        s.add(text)

    while not s.is_empty():
        print(s.remove())

    list_1 = [1, 3, 5]
    list_2 = [1, [3, 5], 7]
    list_3 = [1, [3, [5, 7], 9], 11]
    list_stack(list_1, s)
    list_stack(list_2, s)
    list_stack(list_3, s)

