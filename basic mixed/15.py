from os import *
from sys import *
from collections import *
from math import *

def findAllSubarraysWithGivenSum(arr, s):
    # Write your code here.
    summ = 0
    count_s = 0
    for i in range(len(arr)):
        summ = 0
        for j in range(i, len(arr)):
            summ += arr[j]
            if summ == s:
                count_s+=1
                break

    return count_s

# def findAllSubarraysWithGivenSum(n, s):
#     # Write your code here.
#        left=0
#        count=0
#        sum=0
#        for i in range(len(n)):
#            sum+=n[i]
#            while sum>s:
#               sum-=n[left]
#               left+=1
#            if sum==s:
#                count+=1
#        return count