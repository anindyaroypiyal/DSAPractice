from os import *
from sys import *
from collections import *
from math import *

def minimumParentheses(pattern):

    # Write your code here
    # Return the minimum number of parentheses required.
    s = 0
    v = 0
    flag = 0

    for i in range(len(pattern)):
        if (flag == 0) and (pattern[i] == ')'):
            s += 1
        else:
            if pattern[i] == '(':
                flag = 1
                v += 1
            else:
                v -= 1
        if v==0:
            flag = 0
    res = abs(s) + abs(v)
    return res


