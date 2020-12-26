import random

def read_from_ref(path):
    file = open(path, 'r') 
    lines = file.readlines()

    
    
    trace_lst = []
    physical_memory = []

    for line in lines:
        address = line.strip().split(' ')[1]
        trace_lst.append(address)
    file.close()

    # build trace dictionary
    trace_dict = {}
    for trace in trace_lst:
        if trace not in trace_dict:
            l = list(trace)
            s = l[0]
            l = l[1:-3]
            random.shuffle(l)
            res = ''.join(l)
            res = s + res + "000"
            trace_dict[trace] = res


    output_file_name = "new_"+path
    output_file = open(output_file_name, "a")

    for t in trace_lst:
        access_type = random.sample(['I','L','S','M'], 1)[0]
        output_file.write("{} {}\n".format(access_type, trace_dict[t]))

    output_file.close()

    
    



if __name__ == '__main__':
    for t in ["trace1.ref", "trace2.ref", "trace3.ref"]:
        read_from_ref(t)