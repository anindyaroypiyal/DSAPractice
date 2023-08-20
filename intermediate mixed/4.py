from os import *
from sys import *
from collections import *
from math import *

def removeOutsideRange(root, min, max):
    # write yout code here
    if not root:
        return None
    
    if root < min:
       return removeOutsideRange(root.right, min, max)
    if root > max:
        return removeOutsideRange(root.left, min, max)

    root.left = removeOutsideRange(root.left, min, max)
    root.right = removeOutsideRange(root.right, min, max)
    
    return root
