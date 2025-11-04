def process_matrix(arr, n):
    
    result = [row[:] for row in arr]
    
    for i in range(n):
        for j in range(n):

            if i == j:
                result[i][j] += 1
            
            if i + j == n - 1:
                result[i][j] -= 1
            
            if i < j and i < n - 1 - j:
                result[i][j] += 2
            
            if i > j and i > n - 1 - j:
                result[i][j] -= 2
            
            if j < i and j < n - 1 - i:
                result[i][j] += 3
            
            if j > i and j > n - 1 - i:
                result[i][j] -= 3
    
    return result
