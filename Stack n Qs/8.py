from os import *
from sys import *
from collections import *
from math import *
from queue import Queue

# def reverseQueue(q):
# 	if q.empty():
# 		return -1
# 	temp = q.queue[0]
# 	q.get()
	
# 	reverseQueue(q)
	
# 	q.put(temp)
# 	return q

def reverseQueue(q):
	stack = []
	while not q.empty():
		
		stack.append(q.queue[0])
		q.get()
		
	while len(stack) != 0:
		q.put(stack[-1])
		stack.pop()
	return q
	