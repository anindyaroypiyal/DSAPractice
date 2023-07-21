from os import *
from sys import *
from collections import *
from math import *

'''
    Following is the Binary Tree node structure:
    class TreeNode:
        def __init__(self, data=0, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
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
