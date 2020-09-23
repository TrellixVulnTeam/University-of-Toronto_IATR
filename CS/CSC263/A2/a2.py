def make_weight_balanced_tree(nodes):
    if len(nodes) == 0:
        return NIL
    else:
        median = len(nodes) // 2
        t = TreeNode(nodes[median])
        t.left = make_weight_balanced_tree(nodes[:median])
        t.right = make_weight_balanced_tree(nodes[median+1:])








#q2 part b
#t is the given BST, and total_price is m
def find_two_items(t, m):
    #Make a chained hashtable whose hash function is h(k) = k
    hash_table = make_hash_table();
    for node in t:
        CHAINED_HASH_INSERT(hash_table, node.key)
    for price in hash_table:
        if m - price in hash_table and len(hash_table[m - price]) != 0:
            return hash_table[price][0], hash_table[m - price][0]

def hash(L):
    hash = 5381
    for num in L:
        hash = hash * 33 + num
    return hash

def find(L,m):
    i = 0
    j = len(L) - 1
    while i != j:
        if L[i] + L[j] > m:
            j -= 1
        elif L[i] + L[j] < m:
            i += 1
        else:
            return (L[i],L[j])
    return "no such items"