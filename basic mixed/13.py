from math import *
from collections import *
from sys import *
from os import *

def missingAndRepeating(arr, n):
    # Write your code here

    countNum = [0]*n

    for i in range(n):
        countNum[arr[i]-1] += 1

    m = -1
    r = -1

    for i in range(n):
        if (countNum[i] == 0):
            m = i + 1
        if (countNum[i] == 2):
            r = i + 1

    return [m, r]