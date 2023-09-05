from typing import List
from collections import defaultdict

def smallestSubarrayWithKDistinct(arr: List[int], k: int) -> List[int]:
    # Write your code here.
    st = 0
    ed = len(arr)

    i,j=0,0
    hm = defaultdict(int)

    while (j < len(arr)):
        hm[arr[j]] += 1
        j+=1
  
        if len(hm) < k:
            continue

        while(len(hm) == k):
            windowLen = (j-1)-i+1
            subArrayLen = ed - st + 1
            
            if windowLen < subArrayLen:
                st = i
                ed = j-1
            
            if hm[arr[i]] == 1:
                del hm[arr[i]]
            else:
                hm[arr[i]]-=1
            
            i+=1

    if (st == 0 and ed == len(arr)):
        return [-1]

    else:
        return [st, ed]