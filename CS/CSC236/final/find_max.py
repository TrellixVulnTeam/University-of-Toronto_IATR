def find_max(A,b,e):
    if len(A) == 0:
        return None
    elif b == e:
        return A[b]
    else:
        m = (b + e)//2
        
        left_max = find_max(A,b,m)
        right_max = find_max(A,m+1,e)
        
        max_l = 0
        l_cur = m - 1
        counter_1 = 0
        
        while l_cur >= 0:
            counter_1 = counter_1 + A[l_cur]
            if counter_1 > max_l:
                max_l = counter_1
            l_cur -= 1
        
        max_r = 0   
        r_cur = m + 1
        counter_2 = 0
        
        while r_cur <= len(A) -1:
            counter_2 = counter_2 + A[r_cur]
            if counter_2 > max_r:
                max_r = counter_2
            r_cur += 1
            
        sum = max_l + max_r + A[m]
        
        return max(left_max, right_max, sum)