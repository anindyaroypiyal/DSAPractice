from os import *
from sys import *
from collections import *
from math import *

'''
  ----Binary tree node class for reference-----
    class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''
def findMin(root):
  if not root.left:
    return root.data
  return findMin(root.left)

def bstDelete(root, key):

    # Write your code here.
    if key < root.data:
      if root.left:
        root.left = bstDelete(root.left, key)
    
    elif key > root.data:
      if root.right:
        root.right = bstDelete(root.right, key)

    else:
      if root.left is None and root.right is None:
        return None
      if root.left is None:
        return root.right
      if root.right is None:
        return root.left

      min_val = findMin(root.right)
      root.data = min_val
      root.right = bstDelete(root.right, min_val)

    return root