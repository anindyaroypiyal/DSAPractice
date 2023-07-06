from os import *
from sys import *
from collections import *
from math import *

def findKthElement(matrix, k):

    # Write your code here
    # Return k'th element in spiral form of matrix
    i = 0
    j = 0
    new_arr = []
    c=0
    col_left = -1
    row_up = 0


    row  = len(matrix)
    col = len(matrix[0])

    while(True):
        while (j < col):
            new_arr.append(matrix[i][j])
            c += 1
            if (c == k):
                return ((matrix[i][j]))
            j+=1
        i += 1
        j -= 1
        while(i < row):
            new_arr.append(matrix[i][j])
            c += 1
            if (c == k):
                return ((matrix[i][j]))
            i+=1
        j -= 1
        i -= 1
        while(j > col_left):
            new_arr.append(matrix[i][j])
            c += 1
            if (c == k):
                return ((matrix[i][j]))
            j-=1
        i -= 1
        j+=1
        while(i > row_up):
            new_arr.append(matrix[i][j])
            c += 1
            if (c == k):
                return ((matrix[i][j]))
            i -= 1

        i+=1
        j+=1
        row -= 1
        col -= 1
        col_left += 1
        row_up += 1
    
    # print(new_arr)
