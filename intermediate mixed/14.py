from os import *
from sys import *
from collections import *
from math import *

class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right

def mergeTrees(root1, root2):
    if root1==None and root2==None:
        return None
    if root1==None:
        return root2
    if root2==None:
        return root1
    node=BinaryTreeNode(root1.data+root2.data)
    node.left=mergeTrees(root1.left,root2.left)
    node.right=mergeTrees(root1.right,root2.right)
    return node