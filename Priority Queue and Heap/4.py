from os import *
from sys import *
from collections import *
from math import *
import heapq

def mergeKSortedArrays(kArrays, k:int):

	heap = []
	for i in kArrays:
		heap+=i


	res = []
	heapq.heapify(heap)



	for i in range(len(heap)):
		res.append(heapq.heappop(heap))

	return res

# import heapq
# listForTree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]    
# heapq.heapify(listForTree)             # for a min heap
# heapq._heapify_max(listForTree)        # for a maxheap!!

# heapq.heappop(minheap)      # pop from minheap
# heapq._heappop_max(maxheap) # pop from maxheap

