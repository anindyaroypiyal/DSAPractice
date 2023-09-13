from os import *
from sys import *
from collections import *
from math import *


def subsequences(str):
    res=[]
    ans=""

    def solve(idx,ans):
        if idx==len(str):
            if len(ans)!=0:
                res.append(ans)       
            return
        solve(idx+1,ans+str[idx]) 
        solve(idx+1,ans)

    
    solve(0,ans)
    return res
