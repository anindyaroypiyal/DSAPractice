from os import *
from sys import *
from collections import *
from math import *

# Binary tree node class for reference
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def lowestCommonAncestor(root, x, y):
	# Write your code here.
    def get_lca(node):
        if not node or node.data in (x, y):
            return node

        left = get_lca(node.left)
        right = get_lca(node.right)

        return node if left and right else left or right

    return get_lca(root).data
        