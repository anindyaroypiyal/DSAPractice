from os import *
from sys import *
from collections import *
from math import *

class BinaryTreeNode:
    def __init__(self, data, l=None, r=None):
        self.data = data
        self.left = l
        self.right = r


def BTtoDLL(root):
    # Write your code here.

    # first make inOrderTraversal array from the BT.
    # then make doubly linked list form the array.

    arr = inOrderTr(root)
    
    head = BinaryTreeNode(0) #dummy node
    temp = head #temp for traversing and adding the new nodes to the linked list

    for i in arr:
        temp.right = BinaryTreeNode(i, temp) #we are adding previous==l while making the node.
        temp = temp.right #adding the next==r to the linked list.
    return head.right #return the next of dummy node.

def inOrderTr(root):
    elems = []

    if not root:
        return []

    elems += inOrderTr(root.left)
    elems.append(root.data)
    elems += inOrderTr(root.right)

    return elems
    