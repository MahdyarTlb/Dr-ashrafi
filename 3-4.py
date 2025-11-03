def fact_with_array(n):
    if n < 0 or n > 100:
        raise ValueError("n must be between 1 and 100")
    
    digits = [1]
    
    for x in range(2, n + 1):
        carry = 0
        
        for i in range(len(digits)):
            product = digits[i] * x + carry
            digits[i] = product % 10
            carry = product // 10
        
        while carry > 0:
            digits.append(carry % 10)
            carry //= 10
    
    return ''.join(map(str, digits[::-1]))

print(fact_with_array(5))
print(fact_with_array(100))