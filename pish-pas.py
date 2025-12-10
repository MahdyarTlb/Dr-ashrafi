def prefix_to_infix(e):
    if not e.strip():
        raise ValueError("empty")
    
    tokens = e.split()[::-1]
    stack = []
    
    for token in tokens:
        if token in ['+', '-', '*', '/']:
            
            if len(stack) < 2:
                raise ValueError("operators ins not enough")
            
            op1 = stack.pop()
            op2 = stack.pop()
            
            expr = f"({op1} {token} {op2})"
            stack.append(expr)
        elif token.isdigit():
            stack.append(token)
            
        else:
            raise ValueError(f"in chie?? {token}")
        
    if len(stack) != 1:
        raise ValueError("invalid input")
    
    result = stack[0]
    if result.startswith('(') and result.endswith(')'):
        result = result[1:-1]
    return result
    
def suffix(e):
    
    if not e.strip():
        raise ValueError("empty")
    
    my_stack = []
    
    tokens = e.strip().split()
        
    for token in tokens:
        if token.isdigit():
            my_stack.append(int(token))
        elif token in ['+', '-', '*', '/']:
            
            if len(my_stack) < 2:
                raise ValueError("operators ins not enough")
            
            num1 = my_stack.pop()
            num2 = my_stack.pop()
            
            expr = f"({num1} {token} {num2})"
            my_stack.append(expr)
        else:
            raise ValueError(f"in chie {token}")
            
    return my_stack[0]

    
def precedence(op):
    if op in ['+', '-']:
        return 1
    if op in ['*', '/']:
        return 2
    return 0

def infix_to_prefix(e):
    
    if not e.strip():
        raise ValueError("empty")
    
    expr_stack = []
    ops = []
    counter = 0
    
    tokens = e.split()

    for token in tokens:
        if token.isdigit():
            expr_stack.append(token)

        elif token == '(':
            ops.append(token)
            counter += 1

        elif token == ')':
            if counter == 0:
                raise ValueError("parantez ziad zadi mashti")
            
            while ops and ops[-1] != '(':
                
                if len(expr_stack) < 2:
                    raise ValueError("operator kafi nis")
                
                b = expr_stack.pop()
                a = expr_stack.pop()
                op = ops.pop()
                expr_stack.append(f"{op} {a} {b}")
            if not ops:
                raise ValueError("parantez ( gom shode")
            
            counter -= 1
            ops.pop()
        else:
            while (ops and ops[-1] != '(' and 
                   precedence(ops[-1]) >= precedence(token)):
                
                if len(expr_stack) < 2:
                    raise ValueError("ye chizi kharabe")
                
                b = expr_stack.pop()
                a = expr_stack.pop()
                op = ops.pop()
                expr_stack.append(f"{op} {a} {b}")
            ops.append(token)

    while ops:
        
        if len(expr_stack) < 2:
            raise ValueError("ye chizi kharabe")
        if counter != 0:
            raise ValueError("parantez kharab")
        
        b = expr_stack.pop()
        a = expr_stack.pop()
        op = ops.pop()
        expr_stack.append(f"{op} {a} {b}")

    return expr_stack[0]


def infix_to_post(e):
    
    if not e.strip():
        raise ValueError("mashti inja hichizi naneveshti ke!")

    expr_stack = []
    ops = []
    counter = 0
    
    tokens = e.split()

    for token in tokens:
        if token.isdigit():
            expr_stack.append(token)

        elif token == '(':
            ops.append(token)
            counter += 1

        elif token == ')':
            if counter == 0:
                raise ValueError("parantez ziad zadi mashti! ) kojas?")

            while ops and ops[-1] != '(':
                if len(expr_stack) < 2:
                    raise ValueError("operator kafi nis! do ta adad nadari ke jam koni?")

                b = expr_stack.pop()
                a = expr_stack.pop()
                op = ops.pop()
                expr_stack.append(f"{a} {b} {op}")
            
            if not ops:
                raise ValueError("parantez ( gom shode! koja rafti dige?")

            ops.pop()
            counter -= 1

        elif token in '+-*/':
            while (ops and ops[-1] != '(' and 
                   precedence(ops[-1]) >= precedence(token)):
                
                if len(expr_stack) < 2:
                    raise ValueError("ye chizi kharabe! do ta adad baraye in operator nadari")

                b = expr_stack.pop()
                a = expr_stack.pop()
                op = ops.pop()
                expr_stack.append(f"{a} {b} {op}")
            ops.append(token)
            
        else:
            raise ValueError(f"chi neveshti inja?! '{token}' chie akhe?")

    while ops:
        if ops[-1] == '(':
            raise ValueError("parantez ( baz moonde! ) ro faramoosh kardi mashti")
        
        if len(expr_stack) < 2:
            raise ValueError("adad kam dari! operatora ziadan")

        b = expr_stack.pop()
        a = expr_stack.pop()
        op = ops.pop()
        expr_stack.append(f"{a} {b} {op}")

    if counter != 0:
        raise ValueError("parantezha motavazen nistan! yeki baz ya ziad munde")

    if len(expr_stack) != 1:
        raise ValueError("ye chizi ghalate! natije bayad yek chiz bashe, inja chandta shode")

    return expr_stack[0]

print(infix_to_prefix("10 / ( 5 - 3 )"))
print(infix_to_post("10 / ( 5 - 3 )"))
print(prefix_to_infix("/ 10 + 5 2"))
print(suffix("2 5 8 1 + * /"))