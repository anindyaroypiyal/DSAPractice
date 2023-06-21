from os import *
from sys import *
from collections import *
from math import *

def isPossible(arr, n):
    # Write your code here.
    points = 0
    prev = +inf
    for i in range(n-1, -1, -1):

        if arr[i] < arr[i-2]:
            points -= 1
        if arr[i] <= prev:
            points += 1
        else:
            points -= 1
        prev = arr[i]
    if points < n-2:
        return False
    else:
        return True
        
