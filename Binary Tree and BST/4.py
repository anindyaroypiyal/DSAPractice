from os import *
from sys import *
from collections import *
from math import *

# BinaryTreeNode class definition
# class BinaryTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#

def zigZagTraversal(root):
    ans = []
    left_to_right = []
    right_to_left = []

    if root is None:
        return ans

    left_to_right.append(root)

    while left_to_right or right_to_left:

        while left_to_right:
            root = left_to_right.pop()
            ans.append(root.data)

            if root.left:
                right_to_left.append(root.left)
            if root.right:
                right_to_left.append(root.right)

        while right_to_left:
            root = right_to_left.pop()
            ans.append(root.data)

            if root.right:
                left_to_right.append(root.right)
            if root.left:
                left_to_right.append(root.left)
    return ans