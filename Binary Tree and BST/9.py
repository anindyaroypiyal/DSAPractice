from os import *
from sys import *
from collections import *
from math import *

# Binary Tree node structure
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


def LCAinaBST(root, P, Q):

    # Write your code here
    # P and Q are the given nodes
    # Return LCA node

    if root is None:
        return None
       
    if P.data < root.data and Q.data < root.data:
       return LCAinaBST(root.left, P, Q)

    if P.data > root.data and Q.data > root.data:
       return LCAinaBST(root.right, P, Q)
    
    return root
