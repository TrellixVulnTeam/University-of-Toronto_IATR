import math
def t(x):
    if x == 0:
        return 1
    elif x == 4:
        return 1
    elif x == 6:
        return 1
    elif x == 8:
        return 1
    else:
        if x % 4 == 0:
            return t(x-12) + 1
        else:
            return t(x-6)
        
        
def f(x):
    if x == 0 or x == 2:
        return 0
    elif x == 4:
        return 1
    elif x == 6:
        return 1
    elif x == 8:
        return 1
    else:
        if x % 4 == 0: # if x could be divided by 4
            return f(x-6) + 1 # 1 means the number of way that is all 4-cent, 
                              # f(x-6) means the number of ways that have at least one 6-cent.
        else:
            return f(x-6) 

def f_2(x):
    if x == 4:
        return 1
    elif x == 6:
        return 1
    elif x == 8:
        return 1
    else:
        if x % 4 == 0: # if x could be divided by 4
            return f(x-6) + 1 # 1 means the number of way that is all 4-cent, 
                              # f(x-6) means the number of ways that have at least one 6-cent.
        else:
            return f(x-6) 
        

def g(n):
    if n < 12:
        return 1
    else:
        if n % 12 == 2:
            return g(n-6)
        else:
            return g(n-12)+1
        
def test():
    return all([g(x) == f(x) for x in range(6,1000,2)])


# 和上面无关
def find(A):
    max = 0
    for i in range(len(A)):
        sum = 0
        for j in range(i,len(A)):
            sum += A[j]
            if sum > max:
                max = sum
    return max



#Q5

def distance(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5



def find_closest(A):
    n = len(A)
    res = (A[0],A[1])
    dis = distance(A[0],A[1])
    
    i = 0
    
    while i < n:
        for j in range(i+1,n):
            if distance(A[i],A[j]) < dis: 
                res = (A[i],A[j]) 
                dis = distance(A[i],A[j])
        i += 1
    
    return res

def s(n):
    if n == 4:
        return 1
    elif n == 6:
        return 1
    elif n == 8:
        return 1
    elif n == 10:
        return 2
    elif n == 12:
        return 2
    else:
        if  n % 12 ==2:
            tem_res = n // 12
        else:
            tem_res = n//12 + 1        
        
        return tem_res + s(n-10) 
        # tem_res means the number of ways that n is composed only by 4-cent and 6-cent,
        # s(n-10) means the number of ways that have at least one 10-cent.

def k_2(n):
    if n == 2:
        return 0
    elif n == 4:
        return 1
    elif n == 6:
        return 1
    elif n == 8:
        return 1
    elif n == 10:
        return 2
    else:
        return f_2(n) + k_2(n-10) 
        
def test_2():
    return all([f(n) == new(n) for n in range(4,100,2)])

def test_3():
    return [ (f(n)) for n in range(4,100,2)]

def test_4():
    return [new(n) for n in range(4,100,2)]

def new(n):
    if  n % 12 ==2:
        return n // 12
    else:
        return n//12 + 1
    
    
def s_2(n):

    if n == 4:
        return 1
    elif n == 6:
        return 1
    elif n == 8:
        return 1
    elif n == 10:
        return 2
    elif n == 12:
        return 2
    else:
        if  n % 12 ==2:
            tem_res = n // 12
        else:
            tem_res = n//12 + 1        
        
        return tem_res + s_2(n-10) 
    
    
def m(x):
    if x == 4:
        return 1
    elif x == 6:
        return 1
    elif x == 8:
        return 1
    else:
        if x % 6 == 0: # if x could be divided by 4
            return m(x-4) + 1 # 1 means the number of way that is all 4-cent, 
                              # f(x-6) means the number of ways that have at least one 6-cent.
        else:
            return m(x-4) 