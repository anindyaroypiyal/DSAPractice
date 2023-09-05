from os import *
from sys import *
from collections import *
from math import *
from collections import defaultdict

def countDistinctElements(arr, k):
    # Write your code here

    ans = []
    hm = defaultdict(int)
    i,j = 0,0

    while j < len(arr):
        hm[arr[j]]+=1
        j+=1

        if (j - 1 - i + 1) < k:  #(j - 1 - i + 1) == window size: as j has already increamented we -1 from j.
            continue
        if (j - 1 - i + 1) == k:
            ans.append(len(hm))

            if hm[arr[i]] == 1:
                del hm[arr[i]]
            else:
                hm[arr[i]] -= 1

            i+=1 
    return ans
