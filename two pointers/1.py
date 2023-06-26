from os import *
from sys import *
from collections import *
from math import *

def pairSum(arr, n, target):
    # Write your code here.
    i = 0
    j = len(arr) - 1
    count = 0

    while i < j:
        if arr[i] + arr[j] == target:
            count += 1
            i+=1
            j-=1
        elif arr[i] + arr[j] < target:
            i+=1
        else:
            j-=1
    
    if count == 0:
        return (-1)
    else:
        return (count)