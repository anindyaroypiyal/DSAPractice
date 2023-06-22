from math import *
from collections import *
from sys import *
from os import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
	# Write your code here.
    row = len(matrix)
    col = len(matrix[0])
    o_i = []
    o_j = []

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                o_i.append(i)
                o_j.append(j)
    # print(o)
    for i in range(row):
        for j in range(col):
            if (i in o_i) or (j in o_j):
                matrix[i][j] = 0
    return (matrix)
                
