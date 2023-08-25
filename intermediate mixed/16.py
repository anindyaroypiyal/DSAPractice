from os import *
from sys import *
from collections import *
from math import *

def getLengthofLongestSubstring(s, k):


    # Write your code here.
    curr = 0
    mx = 0
    j = 0
    char_map = {}


    n = len(s)


    for i in range(n):
        if s[i] not in char_map:
            char_map[s[i]] = 1
        else:
            char_map[s[i]] += 1


        if len(char_map) > k:
            while len(char_map) > k:
                char_map[s[j]] -= 1
                if char_map[s[j]] == 0:
                    del char_map[s[j]]
                j += 1


        curr = sum(char_map.values())
        mx = max(mx, curr)
    return mx