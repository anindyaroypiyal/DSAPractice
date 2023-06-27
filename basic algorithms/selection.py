from os import *
from sys import *
from collections import *
from math import *

def selectionSort(arr,n):
    # Write your code here
    # Do not return anything. Update the given array in-place
    
    
    for i in range(0, len(arr)-1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    