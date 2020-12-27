"""
Code for compressing and decompressing using Huffman compression.
"""

from nodes import HuffmanNode, ReadNode


# ====================
# Helper functions for manipulating bytes


def get_bit(byte, bit_num):
    """ Return bit number bit_num from right in byte.

    @param int byte: a given byte
    @param int bit_num: a specific bit number within the byte
    @rtype: int

    >>> get_bit(0b00000101, 2)
    1
    >>> get_bit(0b00000101, 1)
    0
    """
    return (byte & (1 << bit_num)) >> bit_num


def byte_to_bits(byte):
    """ Return the representation of a byte as a string of bits.

    @param int byte: a given byte
    @rtype: str

    >>> byte_to_bits(14)
    '00001110'
    """
    return "".join([str(get_bit(byte, bit_num))
                    for bit_num in range(7, -1, -1)])


def bits_to_byte(bits):
    """ Return int represented by bits, padded on right.

    @param str bits: a string representation of some bits
    @rtype: int

    >>> bits_to_byte("00000101")
    5
    >>> bits_to_byte("101") == 0b10100000
    True
    """
    return sum([int(bits[pos]) << (7 - pos)
                for pos in range(len(bits))])

# ====================
# Helper Class: Priority Queue

class PriorityQueue:
    """ A Priority Queue to collect data
    """
    def __init__(self):
        """ Initialize a new Priortity Queue.

        @param PriorityQueue self: The PriortityQueue itself.
        @rtype: None
        """
        self.list = []

    def add(self, obj):
        """ Add obj to Priority_Queue.

        """
        self.list.append(obj)

    def remove(self):
        """
        Remove smallest item.
        """
        self.list.sort()
        return self.list.pop(0)

    def if_len_1(self):
        """
        Reture True iff the Priority Queue is empty.
        """
        return len(self.list) == 1

# ====================
# Functions for compression


def make_freq_dict(text):
    """ Return a dictionary that maps each byte in text to its frequency.

    @param bytes text: a bytes object
    @rtype: dict{int,int}

    >>> d = make_freq_dict(bytes([65, 66, 67, 66]))
    >>> d == {65: 1, 66: 2, 67: 1}
    True
    """
    res = {}
    text = list(text)
    for item in text:
        if item in res:
            res[item] += 1
        else:
            res[item] = 1
    return res

# the idea below refers wikipedia


def huffman_tree(freq_dict):
    """ Return the root HuffmanNode of a Huffman tree corresponding
    to frequency dictionary freq_dict.

    @param dict(int,int) freq_dict: a frequency dictionary
    @rtype: HuffmanNode

    >>> freq = {2: 6, 3: 4}
    >>> t = huffman_tree(freq)
    >>> result1 = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
    >>> result2 = HuffmanNode(None, HuffmanNode(2), HuffmanNode(3))
    >>> t == result1 or t == result2
    True
    """
    a = PriorityQueue()
    for item in freq_dict:
        a.add([freq_dict[item], HuffmanNode(item)])
    # build huffman_tree
    while not a.if_len_1():
        tp_1 = a.remove()
        tp_2 = a.remove()
        tp_new = [tp_1[0] + tp_2[0], HuffmanNode(None, tp_1[1], tp_2[1])]
        a.add(tp_new)

    return a.list[0][1]


def get_codes(tree):
    """ Return a dict mapping symbols from tree rooted at HuffmanNode to codes.

    @param HuffmanNode tree: a Huffman tree rooted at node 'tree'
    @rtype: dict(int,str)

    >>> tree = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
    >>> d = get_codes(tree)
    >>> d == {3: "0", 2: "1"}
    True
    >>> tree2 = HuffmanNode(None, HuffmanNode(None,HuffmanNode(1),\
    HuffmanNode(2)), HuffmanNode(3))
    >>> d2 = get_codes(tree2)
    >>> d2 == {1: '00',2:'01',3:'1'}
    True
    """
    res = {}
    code_list = create_tag(tree, '')
    for i in range(0, len(code_list), 2):
        res[code_list[i]] = code_list[i+1]
    return res


def create_tag(t, tag):
    if t.is_leaf():
        return [t.symbol, tag]
    else:
        return create_tag(t.left, tag=tag + '0') + create_tag(t.right,
                                                              tag=tag+'1')


def number_nodes(tree):
    """ Number internal nodes in tree according to postorder traversal;
    start numbering at 0.

    @param HuffmanNode tree:  a Huffman tree rooted at node 'tree'
    @rtype: NoneType

    >>> left = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
    >>> right = HuffmanNode(None, HuffmanNode(9), HuffmanNode(10))
    >>> tree = HuffmanNode(None, left, right)
    >>> number_nodes(tree)
    >>> tree.left.number
    0
    >>> tree.right.number
    1
    >>> tree.number
    2
    """
    node_lst = get_internal_node(tree)
    for i in range(len(node_lst)):
        node_lst[i].number = i

# helper for number_nodes, to get internal node list.
def get_internal_node(t):
    if t is None:
        return []
    elif t.is_leaf():
        return []
    else:
        return get_internal_node(t.left) + get_internal_node(t.right) + [t]


def avg_length(tree, freq_dict):
    """ Return the number of bits per symbol required to compress text
    made of the symbols and frequencies in freq_dict, using the Huffman tree.

    @param HuffmanNode tree: a Huffman tree rooted at node 'tree'
    @param dict(int,int) freq_dict: frequency dictionary
    @rtype: float

    >>> freq = {3: 2, 2: 7, 9: 1}
    >>> left = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
    >>> right = HuffmanNode(9)
    >>> tree = HuffmanNode(None, left, right)
    >>> avg_length(tree, freq)
    1.9
    """
    symbol_to_code = get_codes(tree)
    total_bits = 0
    total_fre = 0
    for k in freq_dict:
        total_bits += len(symbol_to_code[k]) * freq_dict[k]
        total_fre += freq_dict[k]
    return total_bits/total_fre


def generate_compressed(text, codes):
    """ Return compressed form of text, using mapping in codes for each symbol.

    @param bytes text: a bytes object
    @param dict(int,str) codes: mappings from symbols to codes
    @rtype: bytes

    >>> d = {0: "0", 1: "10", 2: "11"}
    >>> text = bytes([1, 2, 1, 0])
    >>> result = generate_compressed(text, d)
    >>> [byte_to_bits(byte) for byte in result]
    ['10111000']
    >>> text = bytes([1, 2, 1, 0, 2])
    >>> result = generate_compressed(text, d)
    >>> [byte_to_bits(byte) for byte in result]
    ['10111001', '10000000']
    """
    ori_text = list(text)
    res = []
    total_byte = ''
    for item in ori_text:
        total_byte += codes[item]

    if len(total_byte) % 8 == 0:
        for i in range(0, len(total_byte), 8):
            res.append(bits_to_byte(total_byte[i:i + 8]))
    else:
        remain = len(total_byte) % 8
        last = total_byte[-remain:]
        while len(last) < 8:
            last += '0'

        total_byte = total_byte[:-remain] + last
        for i in range(0, len(total_byte), 8):
            res.append(bits_to_byte(total_byte[i:i + 8]))
    return bytes(res)



def tree_to_bytes(tree):
    """ Return a bytes representation of the tree rooted at tree.

    @param HuffmanNode tree: a Huffman tree rooted at node 'tree'
    @rtype: bytes

    The representation should be based on the postorder traversal of tree
    internal nodes, starting from 0.
    Precondition: tree has its nodes numbered.

    >>> tree = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
    >>> number_nodes(tree)
    >>> list(tree_to_bytes(tree))
    [0, 3, 0, 2]
    >>> left = HuffmanNode(None, HuffmanNode(3), HuffmanNode(2))
    >>> right = HuffmanNode(5)
    >>> tree = HuffmanNode(None, left, right)
    >>> number_nodes(tree)
    >>> list(tree_to_bytes(tree))
    [0, 3, 0, 2, 1, 0, 0, 5]
    """
    res = []
    internal_lst = get_internal_node(tree)
    for node in internal_lst:
        if node.left.is_leaf():
            res.append(0)
        else:
            res.append(1)

        if node.left.is_leaf():
            res.append(node.left.symbol)
        else:
            res.append(node.left.number)

        if node.right.is_leaf():
            res.append(0)
        else:
            res.append(1)

        if node.right.is_leaf():
            res.append(node.right.symbol)
        else:
            res.append(node.right.number)
    return bytes(res)


def num_nodes_to_bytes(tree):
    """ Return number of nodes required to represent tree (the root of a
    numbered Huffman tree).

    @param HuffmanNode tree: a Huffman tree rooted at node 'tree'
    @rtype: bytes
    """
    return bytes([tree.number + 1])


def size_to_bytes(size):
    """ Return the size as a bytes object.

    @param int size: a 32-bit integer that we want to convert to bytes
    @rtype: bytes

    >>> list(size_to_bytes(300))
    [44, 1, 0, 0]
    """
    # little-endian representation of 32-bit (4-byte)
    # int size
    return size.to_bytes(4, "little")


def compress(in_file, out_file):
    """ Compress contents of in_file and store results in out_file.

    @param str in_file: input file whose contents we want to compress
    @param str out_file: output file, where we store our compressed result
    @rtype: NoneType
    """
    with open(in_file, "rb") as f1:
        text = f1.read()
    freq = make_freq_dict(text)
    tree = huffman_tree(freq)
    codes = get_codes(tree)
    number_nodes(tree)
    print("Bits per symbol:", avg_length(tree, freq))
    result = (num_nodes_to_bytes(tree) + tree_to_bytes(tree) +
              size_to_bytes(len(text)))
    result += generate_compressed(text, codes)
    with open(out_file, "wb") as f2:
        f2.write(result)


# ====================
# Functions for decompression


def generate_tree_general(node_lst, root_index):
    """ Return the root of the Huffman tree corresponding
    to node_lst[root_index].

    The function assumes nothing about the order of the nodes in the list.

    @param list[ReadNode] node_lst: a list of ReadNode objects
    @param int root_index: index in the node list
    @rtype: HuffmanNode

    >>> lst = [ReadNode(0, 5, 0, 7), ReadNode(0, 10, 0, 12), \
    ReadNode(1, 1, 1, 0)]
    >>> generate_tree_general(lst, 2)
    HuffmanNode(None, HuffmanNode(None, HuffmanNode(10, None, None), \
HuffmanNode(12, None, None)), \
HuffmanNode(None, HuffmanNode(5, None, None), HuffmanNode(7, None, None)))
    """
    root = node_lst[root_index]

    if root.l_type == 0 and root.r_type == 0:
        return HuffmanNode(None, HuffmanNode(root.l_data),
                           HuffmanNode(root.r_data))
    elif root.l_type == 0 and root.r_type == 1:
        return HuffmanNode(None, HuffmanNode(root.l_data),
                           generate_tree_general(node_lst, root.r_data))
    elif root.l_type == 1 and root.r_type == 0:
        return HuffmanNode(None, generate_tree_general(node_lst, root.l_data),
                           HuffmanNode(root.r_data))
    else:
        return HuffmanNode(None, generate_tree_general(node_lst, root.l_data),
                           generate_tree_general(node_lst, root.r_data))


def generate_tree_postorder(node_lst, root_index):
    """ Return the root of the Huffman tree corresponding
    to node_lst[root_index].

    The function assumes that the list represents a tree in postorder.

    @param list[ReadNode] node_lst: a list of ReadNode objects
    @param int root_index: index in the node list
    @rtype: HuffmanNode

    >>> lst = [ReadNode(0, 5, 0, 7), ReadNode(0, 10, 0, 12), \
    ReadNode(1, 0, 1, 0)]
    >>> generate_tree_postorder(lst, 2)
    HuffmanNode(None, HuffmanNode(None, HuffmanNode(5, None, None), \
HuffmanNode(7, None, None)), \
HuffmanNode(None, HuffmanNode(10, None, None), HuffmanNode(12, None, None)))
    """
    root = node_lst[root_index]

    if root.l_type == 0 and root.r_type == 0:
        return HuffmanNode(None, HuffmanNode(root.l_data),
                           HuffmanNode(root.r_data))
    elif root.l_type == 0 and root.r_type == 1:
        return HuffmanNode(None, HuffmanNode(root.l_data),
                           generate_tree_postorder(node_lst, root_index - 1))
    elif root.l_type == 1 and root.r_type == 0:
        return HuffmanNode(None, generate_tree_postorder(
            node_lst, root_index - 2), HuffmanNode(root.r_data))
    else:
        right_tree = generate_tree_postorder(node_lst, root_index - 1)
        right_tree_internal_node = get_internal_node(right_tree)
        len_r_i_node = len(right_tree_internal_node)
        left_index = root_index - len_r_i_node -1
        return HuffmanNode(None, generate_tree_postorder(node_lst, left_index),
                           generate_tree_postorder(node_lst, root_index - 1))


def generate_uncompressed(tree, text, size):
    """ Use Huffman tree to decompress size bytes from text.

    @param HuffmanNode tree: a HuffmanNode tree rooted at 'tree'
    @param bytes text: text to decompress
    @param int size: how many bytes to decompress from text.
    @rtype: bytes

    >>> freq = {1: 2, 2: 3, 3: 4, 5: 6, 6: 7}
    >>> tree = huffman_tree(freq)
    >>> codes = get_codes(tree)
    >>> codes
    {1: '010', 2: '011', 3: '00', 5: '10', 6: '11'}
    >>> text = bytes([1, 2, 3, 5, 2, 3, 5, 1])
    >>> a = generate_compressed(text, codes)
    >>> b = generate_uncompressed(tree, a, 8)
    >>> list(b)
    [1, 2, 3, 5, 2, 3, 5, 1]
    """
    codes_dict = get_codes(tree)

    # create code to symbol dict
    code_to_symbol_dict = {}
    for k in codes_dict:
        code_to_symbol_dict[codes_dict[k]] = k

    text_to_read = ''.join([byte_to_bits(byte) for byte in text])

    res = []
    num = 0
    new_str = ''
    begin = 0
    while num < size:
        i = 1
        while new_str not in code_to_symbol_dict:
            new_str = text_to_read[begin: begin + i]
            i = i + 1

        res.append(code_to_symbol_dict[new_str])
        num += 1
        begin = begin + i - 1
        new_str = ''
    return bytes(res)


def bytes_to_nodes(buf):
    """ Return a list of ReadNodes corresponding to the bytes in buf.

    @param bytes buf: a bytes object
    @rtype: list[ReadNode]

    >>> bytes_to_nodes(bytes([0, 1, 0, 2]))
    [ReadNode(0, 1, 0, 2)]
    """
    lst = []
    for i in range(0, len(buf), 4):
        l_type = buf[i]
        l_data = buf[i+1]
        r_type = buf[i+2]
        r_data = buf[i+3]
        lst.append(ReadNode(l_type, l_data, r_type, r_data))
    return lst


def bytes_to_size(buf):
    """ Return the size corresponding to the
    given 4-byte little-endian representation.

    @param bytes buf: a bytes object
    @rtype: int

    >>> bytes_to_size(bytes([44, 1, 0, 0]))
    300
    """
    return int.from_bytes(buf, "little")


def uncompress(in_file, out_file):
    """ Uncompress contents of in_file and store results in out_file.

    @param str in_file: input file to uncompress
    @param str out_file: output file that will hold the uncompressed results
    @rtype: NoneType
    """
    with open(in_file, "rb") as f:
        num_nodes = f.read(1)[0]
        buf = f.read(num_nodes * 4)
        node_lst = bytes_to_nodes(buf)
        # use generate_tree_general or generate_tree_postorder here
        tree = generate_tree_general(node_lst, num_nodes - 1)
        size = bytes_to_size(f.read(4))
        with open(out_file, "wb") as g:
            text = f.read()
            g.write(generate_uncompressed(tree, text, size))


# ====================
# Other functions

def improve_tree(tree, freq_dict):
    """ Improve the tree as much as possible, without changing its shape,
    by swapping nodes. The improvements are with respect to freq_dict.

    @param HuffmanNode tree: Huffman tree rooted at 'tree'
    @param dict(int,int) freq_dict: frequency dictionary
    @rtype: NoneType

    >>> left = HuffmanNode(None, HuffmanNode(99), HuffmanNode(100))
    >>> right = HuffmanNode(None, HuffmanNode(101), \
    HuffmanNode(None, HuffmanNode(97), HuffmanNode(98)))
    >>> tree = HuffmanNode(None, left, right)
    >>> freq = {97: 26, 98: 23, 99: 20, 100: 16, 101: 15}
    >>> improve_tree(tree, freq)
    >>> avg_length(tree, freq)
    2.31
    """
    internal_node_list = get_internal_node(tree)[0:-1]

    freq_to_symbol_list = []
    for k in freq_dict:
        freq_to_symbol_list.append((freq_dict[k], k))

    freq_to_symbol_list.sort()
    # freq_to_symbol_list = freq_to_symbol_list[::-1]

    r_internal_node_list = get_internal_node(tree.right)
    l_internal_node_list = internal_node_list[: -len(r_internal_node_list)]


    l_internal_node_list = l_internal_node_list[::-1]
    r_internal_node_list = r_internal_node_list[::-1]

    for node in l_internal_node_list:
        if node.left.is_leaf():
            node.left = HuffmanNode(freq_to_symbol_list.pop()[1])
        if node.right.is_leaf():
            node.right = HuffmanNode(freq_to_symbol_list.pop()[1])
    for node in r_internal_node_list:
        if node.left.is_leaf():
            node.left = HuffmanNode(freq_to_symbol_list.pop()[1])
        if node.right.is_leaf():
            node.right = HuffmanNode(freq_to_symbol_list.pop()[1])

if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config="huffman_pyta.txt")
    # TODO: Uncomment these when you have implemented all the functions
    import doctest
    doctest.testmod()

    import time

    mode = input("Press c to compress or u to uncompress: ")
    if mode == "c":
        fname = input("File to compress: ")
        start = time.time()
        compress(fname, fname + ".huf")
        print("compressed {} in {} seconds."
              .format(fname, time.time() - start))
    elif mode == "u":
        fname = input("File to uncompress: ")
        start = time.time()
        uncompress(fname, fname + ".orig")
        print("uncompressed {} in {} seconds."
              .format(fname, time.time() - start))
