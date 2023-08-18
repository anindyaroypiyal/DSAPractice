from os import *
from sys import *
from collections import *
from math import *

def checkSubset(arr1, arr2, n, m):
    # Write your code here.
    arr1.sort()
    arr2.sort()
    i=0
    j=0
    while (i<n) & (j<m):
        if arr2[j]<arr1[i] :
            return False
        if arr2[j] == arr1[i]:
            i=i+1
            j=j+1
        else:
            i=i+1
    if j>=m:
        return True
