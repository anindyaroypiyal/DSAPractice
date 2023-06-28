from collections import *
from sys import *
from os import *
import math

def findMajorityElement(arr, n):
	# Write your code here.
	maj = 0
	count = 1
	for i in range(1, len(arr)):
		if arr[i] == arr[maj]:
			count += 1
		else:
			count -= 1
		
		if count == 0:
			count = 1
			maj = i

	m = 0
	for i in range(len(arr)):
		if arr[i] == arr[maj]:
			m += 1
	
	condition = math.floor(len(arr)/2)
	if m > condition:
		return (arr[maj])
	else:
		return (-1)