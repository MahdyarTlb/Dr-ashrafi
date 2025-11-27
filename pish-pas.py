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
    
def suffix(e):
    my_stack = []
    
    tokens = e.strip().split()
        
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

    
def precedence(op):
    if op in ['+', '-']:
        return 1
    if op in ['*', '/']:
        return 2
    return 0

def apply_op(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b

def evaluate_infix(expr):
    values = []     
    ops = []        
    
    tokens = expr.split()

    for token in tokens:

        if token.isdigit():
            values.append(int(token))

        elif token == '(':
            ops.append(token)

        elif token == ')':
            while ops and ops[-1] != '(':
                b = values.pop()
                a = values.pop()
                op = ops.pop()
                values.append(apply_op(a, b, op))
            ops.pop()

        else:

            # olaviat balatar
            while ops and precedence(ops[-1]) >= precedence(token):
                b = values.pop()
                a = values.pop()
                op = ops.pop()
                values.append(apply_op(a, b, op))
            ops.append(token)

    while ops:
        b = values.pop()
        a = values.pop()
        op = ops.pop()
        values.append(apply_op(a, b, op))

    return values[0]