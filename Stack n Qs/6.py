from os import *
from sys import *
from collections import *
from math import *
from collections import deque

# Implement class for minStack.
class minStack:

	# Write your code here.
			
    # Constructor
    def __init__(self):
        # Write your code here.
        self._s = deque()
    
    # Function to add another element equal to num at the top of stack.
    def push(self, num: int) -> None:
        # Write your code here.
        self._s.append(num)
    
    # Function to remove the top element of the stack.
    def pop(self) -> int:
        # Write your code here.
        if len(self._s) != 0:
            self._s.pop()
        else: return -1
    
    # Function to return the top element of stack if it is present. Otherwise return -1.
    def top(self) -> int:
        # Write your code here.
        if len(self._s) != 0:
            return (self._s[-1])
        else: return -1
    
    # Function to return minimum element of stack if it is present. Otherwise return -1.
    def getMin(self) -> int:
        # Write your code here.
        if len(self._s) == 0:
            return -1
        else: min(self._s)
