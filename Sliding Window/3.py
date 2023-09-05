from os import *
from sys import *
from collections import *
from math import *
from collections import defaultdict
# import math

def uniqueSubstrings(s ) :
    # Write your code here.

    # longest = 0
    # long_count = 0
    # i,j = 0,0
    # hm = defaultdict(int)

    # while (j<len(input)):
    #     if not hm[input[j]]:
    #         hm[input[j]]+=1
    #         j+=1
        
    #     else:
    #         longest = max(longest, (j - i))  #(j-i)==window size
    #         i = j
    #         hm = defaultdict(int)
    #         print()
    
    # return longest
    #i tried my part above, found some success but not optimal

    charSet = set()
    l = 0
    res = 0
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l+=1
        charSet.add(s[r])
        res = max(res, r-l+1)
    return res
    
        

