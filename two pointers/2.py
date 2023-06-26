from os import *
from sys import *
from collections import *
from math import *

def separateNegativeAndPositive(nums):
    # write your code here
    i = 0
    j = len(nums) - 1
    rearranged = [0]*len(nums)
    
    for item in nums:
        if item < 0:
            rearranged[i] = item
            i += 1
        elif item >= 0:
            rearranged[j] = item
            j -= 1
    
    return(rearranged)
