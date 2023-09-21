from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)
def countWaysToMakeChange(denominations, value) :
    
	# Your code goes here
    cache = {}

    def dfs(i, a):
        if a == value:
            return 1
        if a > value:
            return 0
        if i == len(denominations):
            return 0
        if (i,a) in cache:
            return (cache[(i,a)])
        
        cache[(i,a)] = dfs(i, a+denominations[i]) + dfs(i+1, a)
        return cache[(i,a)]

    return dfs(0,0)

    # TC = O(n * m)

    # for minimum num coin change:

    # dp = [value+1]*(value+1)
    # dp[0] = 0

    # for v in range(1, value+1):
    #     for d in denominations:
    #         if v - d >= 0:
    #             dp[v] = min(dp[v], 1+dp[v-d])

    # print(dp)
    # return dp[value] if dp[value]!=value+1 else -1































#taking inpit using fast I/O
def takeInput() :
    numDenominations = int(input())

    denominations = list(map(int, stdin.readline().strip().split(" ")))

    value = int(input())
    return denominations, numDenominations, value


#main
denominations, numDenomination, value = takeInput()
print((countWaysToMakeChange(denominations, value)))