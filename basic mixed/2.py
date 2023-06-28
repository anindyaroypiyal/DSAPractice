from os import *
from sys import *
from collections import *
from math import *

def findArrayIntersection(arr: list, n: int, brr: list, m: int):
    # Write your code here
    # Return a list containing all the common elements in arr and brr.
    i = 0
    j = 0
    new_arr = []
    # conrer cases 2 ifs
    if (n==0 or m==0):
        return (new_arr)
    
    if(arr[0] > brr[len(brr)-1]) or (brr[0] > arr[len(arr)-1]):
        return (new_arr)

    while (i < len(arr) and j < len(brr)):
        if arr[i] < brr[j]:
            i+=1
        elif arr[i] > brr[j]:
            j+=1
        else:
            new_arr.append(arr[i])
            i+=1
            j+=1

    return(new_arr)
