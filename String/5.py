from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(10 ** 7)


def nextLargestPalindrome(s, length):
    # Write your code here.
    # Return the next greater palindrome in the form of a string.
    digit = int(s)

    while(True):
        digit += 1
        s = str(digit)
        if s == s[::-1]:
            break
    return (s)

# not the optimal solution: time litmit exceeded but i think it is correct

























# Taking input using fast I/0
def takeInput():
    N = int(stdin.readline())
    S = stdin.readline().strip()
    return N, S


tc = int(input())
while tc > 0:
    N, S = takeInput()
    S = nextLargestPalindrome(S, N)
    stdout.write(S + "\n")
    tc -= 1
