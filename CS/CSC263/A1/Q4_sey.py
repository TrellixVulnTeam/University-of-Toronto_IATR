def read_median(A):
    
    left = empty_max_heap 
    
    right = empty_min_heap 
    
    median = 0
    
    for i in range(len(A)):
        
        if i == 0:
            median = A[0]
            print(median)
        elif i % 2 ==  1:
            left.heapInsert(min(A[i],median))
            right.heapInsert(max(A[i],median))
            median = (median + A[i]) / 2
            print(median)
        else:
            if A[i] > right[0]:
                median = right[0]
                right[0] = A[i]
                right[0].bubbledown
            elif A[i] < left[0]:
                median = left[0]
                left[0] = A[i]
                left[0].bubbledown
            else:
                median = A[i]
            print(median)
                    
                        
