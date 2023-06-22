from os import *
from sys import *
from collections import *
from math import *

def isMatrixSymmetric(matrix):
    # Write your code here.  
    row = len(matrix)
    col = row

    for i in range(row):
        for j in range(col):
            if matrix[i][j] != matrix[j][i]:
                return False
                
    return True
        
