memory_size = 8

def read_from_ref(path):
    file = open(path, 'r') 
    lines = file.readlines()

    total_count = 0
    hit_count, miss_count = 0, 0
    
    trace_lst = []
    physical_memory = []

    for line in lines:
        # print("Line{}: {}".format(count, line.strip())) 
        total_count +=1
        address = line.strip().split(' ')[1]
        trace_lst.append(address)

    assert(len(trace_lst) == total_count)

    for i in range(len(trace_lst)):
        # print("access trace number: {}, trace is {}\n".format(i+1, trace_lst[i]))
        # print("before:\n")
        # print(physical_memory)
        if trace_lst[i] in physical_memory:
            hit_count +=1
        else:
            miss_count += 1
            if len(physical_memory) < memory_size:
                physical_memory.append(trace_lst[i])
            else:
                # need to replace page
                reversed_remain_trace_lst = trace_lst[i+1:][::-1]

                    
                #find the one in physical memory which will not be used for the longest time in future.
                idx = 0
                invisible_index = 100000
                if physical_memory[idx] in reversed_remain_trace_lst:
                    invisible_index = reversed_remain_trace_lst.index(physical_memory[idx])
                else:
                    invisible_index = -1
                    # physical_memory[idx] = trace_lst[i]
                    # continue

                for j in range(memory_size):
                    if physical_memory[j] in reversed_remain_trace_lst:
                        temp_index = reversed_remain_trace_lst.index(physical_memory[j])
                        if temp_index < invisible_index:
                            idx = j
                            invisible_index = temp_index
                    else:
                        idx = j
                        invisible_index = -1
                # replace
                physical_memory[idx] = trace_lst[i]
        # print("after:\n")
        # print(physical_memory)
        # print("-----------------------------------------------------")

    assert(hit_count + miss_count == total_count)
    hit_rate = hit_count / (hit_count + miss_count)

    print("hit count: {}\n".format(hit_count))
    print("miss count: {}\n".format(miss_count))
    print("hit rate: {}\n".format(hit_rate))





if __name__ == '__main__':
    read_from_ref("trace3.ref")