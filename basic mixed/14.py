from math import *
from collections import *
from sys import *
from os import *

def fourSum(arr, target):
    # Write your code here
    summ_store = []
    arr = sorted(arr)
    
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            p = j + 1
            q = len(arr) - 1
            summ = target - (arr[i] + arr[j])
            summ_store.append(summ)

            while(p < q):
                if (summ == arr[p]+arr[q]):
                    return 'Yes'
                elif (summ < arr[p]+arr[q]):
                    q-=1
                else:
                    p+=1
    return "No"