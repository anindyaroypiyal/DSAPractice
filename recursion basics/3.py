from os import *
from sys import *
from collections import *
from math import *

def findKthElement(arr1, arr2, k):
	# Write your code here.
	# arr1.extend(arr2)
	# arr1.sort()

	# return arr1[k-1] #O(n log N)

	i, j = 0, 0
	checker = 0

	
	while i < len(arr1) and j < len(arr2):
		if arr1[i] <= arr2[j]:
			i+=1
			checker += 1
			if checker == k:
				return arr1[i-1]
		else:
			j+=1
			checker += 1
			if checker == k:
				return arr2[j-1]
	
	while i < len(arr1):
		i+=1
		checker += 1
		if checker == k:
			return arr1[i-1]
		
	while j < len(arr2):
		j+=1
		checker += 1
		if checker == k:
			return arr2[j-1]
		
		

