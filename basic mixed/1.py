from os import *
from sys import *
from collections import *
from math import *

def areAnagram(str1, str2):
    # Write your code here.

    if len(str1) != len(str2):
        return 0
    
    a = sorted(str1)
    b = sorted(str2)

    if a == b:
        return 1
    else:
        return 0
    