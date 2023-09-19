def isInterleave(a, b, c):
    # Write your code here
    if len(a) + len(b) != len(c):
        return False
    
    dp = [[False]*(len(b)+1) for i in range(len(a)+1)]
    dp[len(a)][len(b)] = True

    for i in range(len(a), -1, -1):
        for j in range(len(b), -1, -1):
            if i < len(a) and a[i] == c[i+j] and dp[i+1][j]:
                dp[i][j] = True
            if j < len(b) and b[j] == c[i+j] and dp[i][j+1]:
                dp[i][j] = True
    return dp[0][0]