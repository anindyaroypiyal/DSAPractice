from os import *
from sys import *
from collections import *
from math import *

def isPossible(arr, n):
    # Write your code here.
    move = False
    for i in range(n-1):
        if arr[i] <= arr[i+1]:
            continue
        if move:
            return False
        
        if (i==0) or (arr[i+1]>=arr[i-1]):
            arr[i] = arr[i+1]
        else:
            arr[i+1] = arr[i]
        move = True
    return True
