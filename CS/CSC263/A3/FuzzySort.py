from random import shuffle

def FuzzySort(L):
    if len(L) < 2:
        return L
    else:
        #randomize the input
        shuffle(L)
        
        pivot = L[0] #chose pivot interval
        
        left = [] #create a empty container to store smaller intervals
        right = [] #create a empty container to store bigger intervals
        middle = [] #create a empty container to store overlapping intervals
        
        for interval in L:
            if interval[1] < pivot[0]:
                left.append(interval)
            elif interval[0] > pivot[1]:
                right.append(interval)
            else:
                middle.append(interval)
        
        #recursively call FuzzySort to left and right and then combine middle 
        return FuzzySort(left) + middle + FuzzySort(right) 
    
    
