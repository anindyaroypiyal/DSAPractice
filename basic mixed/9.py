from math import *
from collections import *
from sys import *
from os import *

def lengthOfLongestConsecutiveSequence(arr, n):
    # Write your code here.
    no_dupli = set(arr)
    max_c = 0

    for elem in no_dupli:
        if (elem - 1) in no_dupli:
            continue
        flag = True
        count = 1
        while flag:
            if (elem + 1) in no_dupli:
                count += 1
                elem += 1
            else:
                flag = False
            max_c = max(count, max_c)
    return max_c
