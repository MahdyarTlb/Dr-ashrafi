'''
    ( n  )   
    ( r  )  =  n! / (n-r)! r!
'''

def nCr(n, r):
    
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1
    
    dp = [0] * (r + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        
        for j in range(min(i, r), 0, -1):
            
            dp[j] += dp[j - 1]
    
    return dp[r]