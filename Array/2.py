from os import *
from sys import *
from collections import *
from math import *

from sys import stdin
import sys

def findSecondLargest(sequenceOfNumbers):
    # Write your code here.

    seq = [*set(sequenceOfNumbers)]

    pre_max = max(seq)
    seq.remove(pre_max)

    if len(seq) == 0:
        return -1
    else:
        return (max(seq))
















# Taking input using fast I/O.
def takeInput():
    n = int(input())

    sequenceOfNumbers = list(map(int, input().strip().split(" ")))

    return sequenceOfNumbers, n

# Main.
t = int(input())
while t:
    sequenceOfNumbers, n = takeInput()
    print(findSecondLargest(sequenceOfNumbers))
    t = t-1
