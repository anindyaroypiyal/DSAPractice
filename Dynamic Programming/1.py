from os import *
from sys import *
from collections import *
from math import *

def countDistinctWays(n: int) -> int:
    #  Write your code here.
    one, two = 1,1

    for i in range(n-1):
        temp = one
        one = one + two
        two = temp
    
    return one
