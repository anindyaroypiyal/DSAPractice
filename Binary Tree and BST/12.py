from os import *
from sys import *
from collections import *
from math import *

'''
    Following is the TreeNode class structure
   
    class   TreeNode :
        def __init__(self, data) :
            self.data = data
            self.left = None
            self.right = None

        def __del__(self):
            if self.left:
                del self.left
            if self.right:
                del self.right

'''
def kthSmallest(root, k):

 
# iterative approach, there is also a recursive approach with inorder traverse list
    count=0

    stack=[]

    cur=root
   

    while cur or stack:

        while cur:

            stack.append(cur)

            cur=cur.left


        cur=stack.pop()

        count=count+1

        if count==k:

            return cur.data

        cur=cur.right
