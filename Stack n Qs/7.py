from os import *
from sys import *
from collections import *
from math import *
from collections import deque

from sys import stdin

# def nextGreater(arr,n):
    
    #Your code goes here
    # stk = deque()
    # ans_arr = []

    # for i in range(len(arr)-1,-1,-1):
    #     stk.append(arr[i]) 
    
    # while len(stk) != 0:
    #     c = True
    #     x = (stk.pop())
    #     for i in range(len(stk)-1,-1,-1):
    #         if x < stk[i]:
    #             ans_arr.append(stk[i])
    #             c = False
    #             break
    #     if c:
    #         ans_arr.append(-1)
        
    # return (ans_arr)
    
def nextGreater(arr,n):
    st = []
    for i in range(n-1,-1,-1):
        ele = arr[i]
        if not st:
            arr[i] = -1
            st.append(ele)
        else:
            while st and st[-1]<=arr[i]:
                st.pop()
            if st:
                arr[i] = st[-1]
            else:
                arr[i]  = -1
            st.append(ele)
    return arr

    
    



#Main

t = int(stdin.readline().rstrip())

while t>0:
    
    n=int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    z=(nextGreater(arr,n))
    for i in z:
        print(i,end=" ")
    print()
    
    t -= 1
