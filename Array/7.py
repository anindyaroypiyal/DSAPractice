from os import *
from sys import *
from collections import *
from math import *

def flipBits(arr, n):
    total_one = 0
    net = 0
    maximum = 0
    for bit in arr:
        if bit:
            total_one += 1
            net -= 1
        else:
            net += 1
        maximum = max(maximum, net)
        if net < 0:
            net = 0
    return total_one + maximum