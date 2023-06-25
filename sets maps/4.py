from os import *
from sys import *
from collections import *
from math import *

def subArrayCount(arr, k):

    # Write your code here.
    # Return count of all the subarray that have sum is divisible by 'k'.
    l = len(arr)
    count = 0

    for a in range(l):
        i = a
        sum = 0
        while(i < l):
            sum += arr[i]
            if (sum % k) == 0:
                count += 1
            i += 1

    return (count)


