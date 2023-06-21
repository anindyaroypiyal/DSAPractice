from os import *
from sys import *
from collections import *
from math import *

def convertString(stri):
    # Write your code here
    formatted = ''
    flag = 0
    for i in range(len(stri)):
        if stri[i] != ' ' and flag == 0:
            formatted += stri[i].upper()
            flag = 1
        elif stri[i] == ' ':
            formatted += stri[i]
            flag = 0
        else:
            formatted += stri[i]
            flag = 1
    return (formatted)