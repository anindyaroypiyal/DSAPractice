from os import *
from sys import *
from collections import *
from math import *

# Following is the TreeNode class structure.
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right

def flattenBinaryTree(root):
    # Write your code here.
    pre = preOrder(root)
    # make linked list from this array: pre (the code doeesn't run, runner file problem)
    
    

def preOrder(root):
    if not root:
        return []
    
    elems = []

    # visit root node
    elems.append(root)

    # visit left tree
    elems += preOrder(root.left)

    # visit right tree
    elems += preOrder(root.right)

    return elems