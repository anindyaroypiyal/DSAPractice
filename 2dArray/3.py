from os import *
from sys import *
from collections import *
from math import *

def inplaceRotate(inputArray, n):

    # Write your code here.
    row = len(inputArray)
    col = row
    matrix = []

    for i in range(row):
        r = []
        for j in range(col):
            r.append(0)
        matrix.append(r)
    
    for i in range(row):
        c = col - 1
        for j in range(col):
            matrix[c][i] = inputArray[i][j]
            c -= 1
    return(matrix)
