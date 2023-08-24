from os import *
from sys import *
from collections import *
from math import *
from collections import defaultdict

'''
  ----Binary tree node class for reference-----
    class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''

def bottomRightView(root):

    # Write your code here
    # Return the bottom right view
    d = defaultdict() #for not throwing key error. we will assign the key and the values later.
    view(root, d , 0)
    ans = []
    
    for items in d.values():  #we got our values in the dictionary, now we just put it in array, sort it in increase order and send the array.
      ans.append(items)

    return (sorted(ans))
    

def view(root, d, integer):
  if not root:
    return
  d[integer] = root.data  #the current node data in the dictionary
  view(root.left, d, integer+1) # will iterate through left tree and increse the index val
  view(root.right, d, integer)  #for bottom right we need to replace the values that will be hidden behind.