from os import *
from sys import *
from collections import *
from math import *

def maxProductCount(arr, n):
    # Write your code here.
    d = {}
    
    for i in range(n):
        for j in range(i+1,n):
            d[arr[i]*arr[j]] += 1

    freq = 0
    maxProd = 0

    for item in d:
        if d[item] >= freq:
            if d[item] == freq:
                maxProd = min(maxProd, item)
            else:
                maxProd = item
                freq = d[item]

    if freq > 1:
        totalFreq = (freq * (freq - 1))/2 #nCr: combination
        return [maxProd, totalFreq]
    return 0