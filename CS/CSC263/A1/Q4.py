def read_median(A):
    n = A.length
    
    A = empty_max_heap 
    
    B = empty_min_heap 
    
    median = 0
    
    for i in range(n):
        
        if i == 0:
            median = A[0]
            print(median)
        elif i == 1:
            A.insert(min(A[i],median))
            B.insert(max(A[i],median))
            median = (median + A[i]) / 2
            print(median)
        elif i == 2:
            if A[i] > B[0]:
                median = B[0]
                B[0] = A[i]
            elif A[i] < A[0]:
                median = A[0]
                A[0] = A[i]
            else:
                median = A[i]
            print(median)
            
        else:
            if i % 2 == 1:
                if A[i] > median:
                    A.insert(median)
                    B.insert(A[i])
                else:
                    A.insert(A[i])
                    B.insert(median)
                    
                median = (A[0] + B[0]) / 2
                print(median)
            
            else:
                if A[i] > median:
                    if A[i] < B[0]:
                        median = A[i]
                    else:
                        median = B[0]
                        B[0] = A[i]
                        B[0].bubbledown
                        
                elif A[i] < median:
                    if A[i] > A[0]:
                        median = A[i]
                    else:
                        median = A[0]
                        A[0] = A[i]
                        A[0].bubbledown
                else:
                    median = A[i]
                    
                print(median)
        
                        