from os import *
from sys import *
from collections import *
from math import *

def minCashFlow(money, n):

    # Write your code here.
    arr=[0]*n
    for i in range(n):
        for j in range(n):
            arr[i]-=money[i][j]
            arr[j]+=money[i][j]
    temp=0
    for a in arr:
        if a<0:
            temp+=(a*(-1))
            
    return temp
