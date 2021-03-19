import stack

#if __name__=='__main__':
    #new = stack.Stack()
    #text = input('Type a string:')
    
    #while text != 'end':
        #new.push(text)
        #text = input('Type a string:')
        
    #while not new.is_empty():
        #last = new.pop()
        #print(last
        
        
def stack_list(list,stack):
    '''
    (list,Stack)--> NoneType
    
    Adds each element of the list to the stack.
    Removes the top element from the stack. If the element is a non-list, it prints it. If the element is a list, it stores each of its elements on the stack.
    Continue the previous step until the stack is empty. Check for an empty stack, rather than causing an exception to be raised!
    '''
    for i in list:
        stack.push(i)    

    while not stack.is_empty():
        first = stack.pop()
        if not isinstance(first,list):
            print(first)
        else:
            stack_list(first,stack)
    
                
                
            
    
    
      
    
    
    

    
    