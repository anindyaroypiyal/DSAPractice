from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :

	# Your code here
    # return the answer
    cur_sum = 0
    max_sum = min(arr)
    for i in range(len(arr)):
        cur_sum += arr[i]
        if cur_sum < 0:
            cur_sum = 0
        max_sum = max(cur_sum, max_sum)

    return(max_sum)































#taking inpit using fast I/O
def takeInput() :
	
    n =  int(input())

    if(n == 0) :
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(maxSubarraySum(arr, n))
