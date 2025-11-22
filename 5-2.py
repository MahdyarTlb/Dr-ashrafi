def intersection(stack, queue):
    
    result = []
    
    for item in stack:
        if item in queue and item not in result:
            result.append(item)
    
    print(result)