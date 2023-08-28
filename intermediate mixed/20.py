from os import *
from sys import *
from collections import *
from math import *

def ayushGivesNinjatest(n, m, time):
    # Write your code here.
    minn = max(time)
    maxx = sum(time)
    res = 0

    while minn<=maxx:
        midd = (minn+maxx) // 2
        if (isValid(time,n, midd)):
            res = midd
            maxx = midd - 1
        else:
            minn = midd + 1
    return res

def isValid(time, n, res):
    day = 1
    summ = 0
    for i in range(len(time)):
        if ((summ + time[i]) > res):
            day+=1
            summ = time[i]
        else:
            summ += time[i]
    return day <= n