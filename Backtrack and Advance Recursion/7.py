from os import *
from sys import *
from collections import *
from math import *

def findPermutations(s):
    n = len(s)
    if n == 1:
        return [s]
    arr = [charr for charr in s]
    ans = []
    index = 0
    helper(index, arr, ans, n)
    return ans

def helper(index, arr, ans, n):
    #base case
    if index == n-1:
        ans.append("".join(arr))
        return
    for i in range(index, n):
        #small calculation
        #swap for all possible solution
        arr[index], arr[i] = arr[i], arr[index]
        #recursion call
        helper(index+1, arr, ans, n)
        #backtrack call
        arr[index], arr[i] = arr[i], arr[index]
        