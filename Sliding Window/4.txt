from os import *
from sys import *
from collections import *
from math import *

from sys import stdin
import sys
from collections import defaultdict


def findAnagramsIndices(n, m, st, ptr):

    # Write your code here.
    hm = defaultdict(int)
    a = []

    for i in range(m):   #put all characters of ptr in a map and count how many are there.
        hm[ptr[i]]+=1
    count = len(hm)

    i,j = 0,0
    while(j < n):   #j will traverse till the end of str.
        if st[j] in hm:     #if the value is in hm, then decrease it's occurance. helps us to count the anagram.

            hm[st[j]] -= 1
                                #count and occurance are not same, occurance is for a particular values, and count is for the existence of the value.
            if hm[st[j]] == 0:
                count -= 1      #we crossd it out because in the window we have seen the value.
            
        j+=1        

        if (j-i) < m:       #have'nt reached the window length so keep looking.
            continue

        if (j-i) == m:      #reached the window length.
            if count == 0:  #when count == 0, means in this window an anagram is present.
                a.append(i) #we add the starting of the window to ans list, window size is len(ptr)==m.

            if st[i] in hm:     #before sliding the window we will check if the value in i belongs to our ptr set.
                if hm[st[i]] == 0:  #if any occurence is 0 then only we will increase the count. as we are moving the window and our item is a part of the ptr. we will increase the count and then increase it's occurance.
                    count += 1  #we update the existance as it's no longer will be on the window.
                hm[st[i]]+=1    #increase the  occurence.

        i+=1        #slide the window
    return a        #return the list where ans are stored.



# Taking input using fast I/O.
def takeInput():

    nums = list(map(int, input().strip().split(" ")))
    st = input()
    ptr = input()

    return nums, st, ptr


# Main.
t = int(input())
while t:
    nums, st, ptr = takeInput()
    n, m = nums
    answer = findAnagramsIndices(n, m, st, ptr)
    for ans in answer:
        print(ans, end=" ")
    print()
    t = t-1
