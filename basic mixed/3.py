import math
from collections import *
from sys import *
from os import *

def majorityElementII(arr):
	# Write your code here.
	limit = math.floor(len(arr)/3)

	new_arr = []
	count = 0

	arr.sort()
	prev = arr[0]
	count = 1

	if count > limit:
		new_arr.append(arr[0])

	for i in range(1, len(arr)):
		if (arr[i] == prev):
			count += 1
		else:
			prev = arr[i]
			count = 1

		if count > limit:
			new_arr.append(arr[i])
		
	a = [*set(new_arr)]
	return (a)
		
