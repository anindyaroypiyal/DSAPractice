from os import *
from sys import *
from collections import *
from math import *

def maxSubSumKConcat(arr, n, k):

	# Write your code here.
	arr = arr * k
	
	sum = 0
	max_sum = min(arr)
	for i in range(n * k):
		sum += arr[i]
		max_sum = max(max_sum, sum)
		if sum < 0:
			sum = 0		
	return (max_sum)