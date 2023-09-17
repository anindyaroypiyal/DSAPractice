from sys import stdin
import sys

def cutRod(price, n):

    # Write your code here.
    dp = [0]*(n+1)
    for i in range(1,n+1):
        for j in range(i):
            dp[i] = max(dp[i], price[j]+dp[i-j-1])
    
    # print(dp)
    return dp[-1]

# Taking input using fast I/O.
def takeInput():
    n = int(input())

    price = list(map(int, input().strip().split(" ")))

    return price, n


# Main.
t = int(input())
while t:
    price, n = takeInput()
    print(cutRod(price, n))
    t = t-1
