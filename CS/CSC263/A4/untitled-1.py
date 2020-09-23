#G is graph we create in part(a), L is straight line we get from part(c).

def find_number_of_rows(G,L): 
    # add an attribute called row to each vertex in L, initialized to 1
    for u in L:
        u.row = 1
    
    for u in L:
        for v in G.Adj[u]:
            if u.row >= v.row:
                v.row = u.row + 1
                
    return max([ u.row for u in L])
            
