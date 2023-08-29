from os import *
from sys import *
from collections import *
import math

# Binary tree node class for reference.
class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def inOrder(root):
    if not root:
        return

    inOrder(root.left)

    if ((prev != None) and (root.val > prev.val)):
        # this is first violation. mark first and middle
        if (first == None):
            first = prev
            middle = root
        else: last = root #the second violation while traversing.
    
    prev = root

    inOrder(root.right)

def FixBST(root):
    # Write your code here.
    
    #1 approach would be to store traverse the tree inOrder Traversal, get all the vals in an array.
    # all the values should be in increasing order. if we find a value that is not in increasing order, that means
    # we found what to swap, now find which value to swap with.
    # get these 2 values in list. and swap in the tree on another traversal
    # However this approach will be invalid here, because it will take extra space. This is brute force.
    # we'll see better approach of O(N) time below.

    first, middle, last, prev = None

    inOrder(root)
    if ((first!= None)and(last!=None)):
        first.val, last.val = last.val, first.val
    elif((first!= None)and(middle!=None)):
        first.val, middle.val = middle.val, first.val



# Fast input.
def takeInput():
    arr = list(map(int, stdin.readline().strip().split(" ")))

    rootData = arr[0]

    n = len(arr)

    if(rootData == -1):
        return None

    root = BinaryTreeNode(rootData)
    q = Queue()
    q.put(root)
    index = 1
    while(q.qsize() > 0):
        currentNode = q.get()

        leftChild = arr[index]

        if(leftChild != -1):
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        index += 1
        rightChild = arr[index]

        if(rightChild != -1):
            rightNode = BinaryTreeNode(rightChild)
            currentNode .right = rightNode
            q.put(rightNode)

        index += 1

    return root

# Print the tree nodes.
def printLevelOrder(root):
    q = Queue()
    if(root == None):
        return

    q.put(root)

    while(q.qsize() > 0):
        currentNode = q.get()

        print(currentNode.val, end=" ")

        if(currentNode.left != None):
            q.put(currentNode.left)

        if(currentNode.right != None):
            q.put(currentNode.right)

    print()

# Main.
t = int(input().strip())
for i in range(t):
    root = takeInput()
    root = FixBST(root)
    printLevelOrder(root)