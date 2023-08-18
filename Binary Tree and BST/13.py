from os import *
from sys import *
from collections import *
from math import *


    # ------- Binary Tree node structure -------
class   BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right
      

def predecessorSuccessor(root, key):

	# Write your code here.

    # first make in order traversal list
    def getInOrderTraversal(root):
        # Write your code here.
        if root is None:
            return []

        elems = []

        # visit left tree
        if root.left:
            elems += getInOrderTraversal(root.left)
        # visit root
        elems.append(root.data)
        # visit right tree
        if root.right:
            elems += getInOrderTraversal(root.right)

        return elems

    inOrderList = getInOrderTraversal(root)
    
    # from the list get the item before and after the key
    a = inOrderList.index(key)
    
    if a == 0 or a == len(inOrderList) - 1:
        print('-1')
    else:
        print(inOrderList[a-1])
    
    if a == 0 or a == len(inOrderList) - 1:
        print('-1')
    else:
        print(inOrderList[a+1])
    # print(inOrderList[a+1])