# analysis.py
# instruction to run it:
# 1. Put the trace files in the same directory with this analysis.py file.
# 2. In command line, run python3 analysis.py


def read_from_ref(path):
    file = open(path, 'r') 
    lines = file.readlines()
    # count = 0
    I_count, L_count, S_count, M_count = 0, 0, 0, 0
    
    I_dict = {}
    data_dict = {}

    for line in lines:
        # print("Line{}: {}".format(count, line.strip())) 
        line = line.strip()
        access_type = line[0]
        if access_type == 'I':
            raw_address = line.strip().split('  ')[1][:-2]
        else:
            raw_address = line.strip().split(' ')[1][:-2]
        
        address = raw_address[:-3] + '000'

        if access_type == 'I':
            I_count += 1
        elif access_type == 'L':
            L_count +=1
        elif access_type == 'S':
            S_count +=1
        elif access_type == 'M':
            M_count +=1
        else:
            exit('access type is invalid')

        if access_type == 'I':
            if address not in I_dict:
                I_dict[address] = 1
            else:
                I_dict[address] +=1
        else:
            if address not in data_dict:
                data_dict[address] = 1
            else:
                data_dict[address] +=1

        # print(access_type)
        # print(raw_address)
        # print(address)
        # count+=1;

    file.close()


    file_name = path.strip().split('.')[0]

    output_file = open("analysis.txt", "a")
    output_file.write("Trace file: {}\n".format(file_name))
    output_file.write("\n")
    output_file.write("Counts:\n")
    output_file.write(" Instructions {}\n".format(I_count))
    output_file.write(" Loads {}\n".format(L_count))
    output_file.write(" Stores {}\n".format(S_count))
    output_file.write(" Modifies {}\n".format(M_count))
    output_file.write("\n")

    output_file.write("Instructions:\n")
    for k,v in I_dict.items():
        output_file.write("{},{}\n".format(k, v))

    output_file.write("Data:\n")
    for k,v in data_dict.items():
        output_file.write("{},{}\n".format(k, v))

    output_file.write("\n")
    output_file.close()


if __name__ == '__main__':
    ref_names = ["addr-simpleloop.ref", "addr-matmul.ref", "addr-blocked.ref"]
    for ref_name in ref_names:
        read_from_ref(ref_name)
