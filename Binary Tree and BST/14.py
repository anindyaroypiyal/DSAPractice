from os import *
from sys import *
from collections import *
from math import *

'''

    Following is the Binary Tree Node structure:

    class  TreeNode :
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

def pairSumBST(root, k):

	# Write your code here
    
	# first make inorder traversal (list in increasing order)
    allElems = getInOrderTraversal(root)
    
    # use 2 pointer approach in the list to get the result
    i = 0
    j = len(allElems) - 1

    while i < j:
        res = allElems[i] + allElems[j]
        if res < k:
            i+=1
        elif res > k:
            j-=1
        else:
            return True
    return False
        