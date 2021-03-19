from csc148_queue import Queue

def list_queue(lst, queue):
    for item in lst:
        queue.add(item)


    while not queue.is_empty():
        q_1 = queue.remove()
        if isinstance(q_1, list):
            for item in q_1:
                queue.add(item)
        else:
            print(q_1)



if __name__ == '__main__':
    q = Queue()
    #i = int(input('type a int:'))

    #while i != 148:
    #    q.add(i)
    #    i = int(input('type a int:'))

    #print(sum(q._content))

    list_1 = [1, 3, 5]
    list_2 = [1, [3, 5], 7]
    list_3 = [1, [3, [5, 7], 9], 11]
    #list_queue(list_1, q)
    #list_queue(list_2, q)
    list_queue(list_3, q)



