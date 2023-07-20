from os import *
from sys import *
from math import *
from collections import deque

# Binary tree node class for reference
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# def getLeftView(root)->list:
#     # Write your code here
#     # Return a list
#     res = []
#     q = deque([root])

#     while q:
#         leftSide = None
#         qlen = len(q)

#         for i in range(qlen):
#             node = q.pop()
#             if node:
#                 leftSide = node
#                 q.append(node.left)
#                 q.append(node.right)
        
#         if leftSide:
#             res.append(leftSide.data)
#     return res

def getLeftView(root)->list:
   # Write your code here
   # Return a list
   sol = []
   if root==None:
       return ""
   def left(root, l):
       if root==None:
           return ""
       if len(sol)==l:
           sol.append(root.data)
       left(root.left, l+1)
       left(root.right, l+1)
   left(root, 0)
   return sol