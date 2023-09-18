from sys import stdin
import sys 
sys.setrecursionlimit(10**7)
# def longestIncreasingSubsequence(arr, n) :

# 	# Your code goes here
#     LIS = [1] * n

#     for i in range(n-1, -1, -1):
#         for j in range(i+1, n):
#             if arr[i] < arr[j]:
#                 LIS[i] = max(LIS[i], 1+LIS[j])

#     return (max(LIS)) 

from sys import stdin
import sys 
sys.setrecursionlimit(10**7)
from bisect import bisect_left

def longestIncreasingSubsequence(arr, n):
    dp = []
    dp.append(arr[0])
    for i in range(1, n):
        if arr[i] > dp[-1]:
            dp.append(arr[i])
        else:
            ind = bisect_left(dp, arr[i])
            dp[ind] = arr[i]

    return len(dp)






























#taking inpit using fast I/O
def takeInput() :
    n = int(input())

    if n==0 :
        return list(), n
        
    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(longestIncreasingSubsequence(arr, n))