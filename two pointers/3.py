from os import *
from sys import *
from collections import *
from math import *

def isSubSequence(str1, str2):

    # Write your code here.
    i = 0
    j = 0
    count = 0
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            i += 1
            count += 1
    if count == len(str1):
        return True
    else:
        return False

