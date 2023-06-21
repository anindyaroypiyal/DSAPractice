from os import *
from sys import *
from collections import *
from math import *

def coverageOfMatrix(mat):

    # Write your code here.
    count=0
    row=len(mat)
    column=len(mat[0])

    for i in range(row):
        for j in range(column):

            if(mat[i][j]==0):
                if(i!=0):
                    count+=mat[i-1][j]

                if(i!=row-1):
                    count+=mat[i+1][j]

                if(j!=0):
                    count+=mat[i][j-1]

                if(j!=column-1):                     
                    count+=mat[i][j+1]

    return count
                