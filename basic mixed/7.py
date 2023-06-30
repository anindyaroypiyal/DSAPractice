from os import *
from sys import *
from collections import *
from math import *

def findTriplet(arr,n):
	# Write your code here
	# Return a list containing either 3 or 0 elements.

	arr.sort()
	new_arr = []

	for i in range(n-1 , -1 , -1):
		first = 0
		second = i-1

		while (first < second):
			if (arr[first] + arr[second] == arr[i]):
				new_arr.append(arr[first])
				new_arr.append(arr[second])
				new_arr.append(arr[i])
				return new_arr
			elif (arr[first] + arr[second] < arr[i]):
				first += 1
			else:
				second -= 1
	return new_arr