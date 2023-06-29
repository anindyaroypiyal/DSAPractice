from os import *
import sys
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def rotateMatRight(mat, n, m, k):
	# Write your code here.
	x = [ [0]*m for i in range(n)]
	new_arr = []
	# return(x)
	for i in range(n):
		for j in range(m):
			a = (j+k) % m
			x[i][a] = mat[i][j]
	
	for i in range(n):
		for j in range(m):
			new_arr.append(x[i][j])
	
	return(new_arr)

# Taking the input.
def takeInput() :
	n, m, k = map(int, sys.stdin.readline().strip().split(" "))
	mat = [list(map(int, sys.stdin.readline().strip().split(" "))) for row in range(n)]
	return n, m, k, mat

# Printing the Matrix.
def printAns(ans):
	for i in ans:
		print(i, end = ' ')
	print('')

# Main.
t = int(input().strip())
for i in range(t):
	n, m, k, mat = takeInput()
	ans = rotateMatRight(mat, n, m, k)
	printAns(ans)