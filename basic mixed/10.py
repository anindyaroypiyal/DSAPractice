from os import *
from sys import *
from collections import *
from math import *
import math

def maxSubSumKConcat(arr, n, k):

	# Write your code here.

	max_c = min(arr)
	summ = 0
	l = len(arr)

	for i in range(l * k):
		summ += arr[i%l]
		max_c = max(summ, max_c)
		if summ < 0:
			summ = 0

	return (max_c)
