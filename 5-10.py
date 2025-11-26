# approach:
#     1. we iterate from right
#     2. if reach a number push it into the stack
#     3. else if we reach to a operator, pop 2 latest numbers and calculate
#     4. push the result



def stack_f(ebarat):
    my_stack = []
    
    tokens = ebarat.strip().split()
    
    tokens.reverse()
    
    for token in tokens:
        if token.isdigit():
            my_stack.append(int(token))
        else:
            num1 = my_stack.pop()
            num2 = my_stack.pop()
            
            if token == '+':
                result = num1 + num2
            elif token == '-':
                result = num1 - num2
            elif token == '*':
                result = num1 * num2
            elif token == '/':
                result = num1 / num2
                
            my_stack.append(result)
            
    print(my_stack[0])
        
        
        
        
ebarat = "* / 5 + 5 5 5"
 
stack_f(ebarat)