from os import *
from sys import *
from collections import *
from math import *

class TreeNode:
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right

def inOrderTr(root):
    elems = []

    if not root:
        return []

    elems+=inOrderTr(root.left)
    elems.append(root.data)
    elems+=inOrderTr(root.right)

    return elems

def mergeBST(root1, root2):
	# Write your code here.
    a1 = inOrderTr(root1)
    a2 = inOrderTr(root2)

    ans = a1 + a2
    return (sorted(ans))

