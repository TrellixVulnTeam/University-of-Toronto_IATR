# Recursive components

# Recursion types
# 1. N-1 approach
# 2. Divide in 2 or more subproblems

# Goal: call itself to solve a smaller part of the problem, using the same function.

# Steps:
# 1. Base case: simplest case, where we stop recursing
# 2. recursive decomposition step: break problem into smaller

# ex sum of elements, using recursing

def sum_list(L):
    if len(L) == 0:
        return 0
    else:
        return L[0] + sum_list(L[1:])

#deal with complex list, ex L = [1, [5,3], 8, [4,[9, 7]]]
# Nested list can occur at any depth, so complicated !!!

#def sun_list(L):
#    if isinstance(L, list):
#        s = 0
#        for elem in L:
#            # calculate the sum of the sublist'elem' recursively
#            s += sum_list(elem)
#        return s
#    else:
#      return L
