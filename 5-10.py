# approach:
#     1. we iterate from right
#     2. if reach a number push it into the stack
#     3. else if we reach to a operator, pop 2 latest numbers and calculate
#     4. push the result



def prefix(e):
    
    op_stack = []      # operators
    val_stack = []     # values
    
    tokens = e.split()

    for token in tokens:
        if token in ['+', '-', '*', '/']:
            op_stack.append(token)
            
        else:
            val_stack.append(int(token))

            while len(val_stack) >= 2 and len(op_stack) >= 1:
                right = val_stack.pop()
                left = val_stack.pop()
                op = op_stack.pop()

                if op == '+': val_stack.append(left + right)
                elif op == '-': val_stack.append(left - right)
                elif op == '*': val_stack.append(left * right)
                elif op == '/': val_stack.append(left / right)

    return val_stack[0]
        
e = "* / 5 + 5 5 5"
prefix(e)