from os import *
from sys import *
from collections import *
from math import *


def rotateArr(size,arr,rotate):

 

    newArr = arr[rotate:]+arr[:rotate]

    string = ""

    string =" ".join(str(v) for v in newArr)

    print(string)

 

size = int(input())

 

arr = list(map(int,input().split()))

 

rotate = int(input())

 

rotateArr(size,arr,rotate)

#Your code goes here.
# size = 8
# arr = [7, 5, 2, 11, 2, 43, 1, 1]
# rotate = 2

# def rotateArray(N,arr,K):
#     arr2 = arr

#     for i in range(N):
#         arr2[i-K] = arr[i]

#     print(arr2)

# N = int(input())
# arr = list(map(int,input().split()))
# K = int(input())

# rotateArray(N,arr,K)


# for i in range (size):
#     pos = i - rotate
#     if (pos) < 0:
#         arr2[size + pos] = arr[i]
#     else:
#         arr2[pos] = arr[i]  

# print(arr2)























