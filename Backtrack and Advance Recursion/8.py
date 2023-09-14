from os import *
from sys import *
from collections import *
from math import *

def generateIPAddress(s):
    # Write your code here.
    res = []

    if len(s) > 12:
        return res
    
    def backTrack(i, dots, curIP):
        if (dots == 4) and i == len(s):
            res.append(curIP[:-1])
            return
        
        if dots > 4:
            return
        
        for j in range(i, min(i+3, len(s))):
            if int(s[i:j+1]) < 256 and (i==j or s[i] != '0'):
                backTrack(j+1, dots+1, curIP + s[i:j+1] + '.')
   
    backTrack(0,0, "")
    return res