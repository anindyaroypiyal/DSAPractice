from os import *
from sys import *
from collections import *
from math import *
from collections import deque

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

class Stack:
    def __init__(self):
        # Intitialize your data structure here.
        self._s = deque()
    def getSize(self):

        # Implement the getSize() function.
        return len(self._s)

    def isEmpty(self):

        # Implement the isEmpty() function.
        if len(self._s) == 0:
            return ("True")
        else: return ("False")

    def push(self,ele):
        # Implement the push() function.
        self._s.append(ele)

    def pop(self):

        # Implement the pop() function.
        if len(self._s) == 0:
            return -1
        return(self._s.pop())

    def top(self):

        # Implement the top() function.
        if len(self._s) == 0:
            return -1
        else: return (self._s[-1])





def takeInput():
    values = list(map(int,stdin.readline().strip().split(" ")))
    return values




#  main
st = Stack()
queries = int(input().strip())
for _ in range(queries):
    values = takeInput()
    if values[0] == 1:
        st.push(values[1])
    elif values[0] == 2:
        print(st.pop())
    elif values[0] == 3:
        print(st.top())
    elif values[0] == 4:
        print(st.getSize())
    else:
        print(st.isEmpty().lower())
