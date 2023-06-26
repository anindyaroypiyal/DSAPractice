from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)


def getGroupedAnagrams(inputStr):
    # Write your code here.
    groups = {}
    groups_list = []

    for item in inputStr:
        
        b = ''.join(sorted(item))
        if b in groups:
            groups[b].append(item)
        else:
            groups[b] = [item]
            
    for v in groups.values():
        groups_list.append(v)
    
    return groups_list
    


def takeInput():

    n = stdin.readline().strip()
    inputStr = list(stdin.readline().strip().split(" "))

    return inputStr, n


def printAnswer(groupedAnagram):
    for group in groupedAnagram:
        group.sort()

    groupedAnagram.sort()

    print('\n'.join(map(' '.join, groupedAnagram)))


T = int(stdin.readline().strip())
for i in range(T):
    inputStr, n = takeInput()
    groupedAnagram = getGroupedAnagrams(inputStr)
    printAnswer(groupedAnagram)
