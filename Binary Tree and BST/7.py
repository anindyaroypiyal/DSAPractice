from os import *
from sys import *
import collections
from math import *

'''
# Binary tree node class for reference
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

def verticalOrderTraversal(root):
    if root is None:
        return
        
    ans = []
    dic = collections.defaultdict(list)

    q=[(root,0)]

    
    while q:
        temp,hd = q.pop(0)

        dic[hd].append(temp.data)

        if temp.left:
            q.append((temp.left,hd-1))
        if temp.right:
            q.append((temp.right, hd+1))

    for i in sorted(dic.keys()):
        for j in dic.get(i):
            ans.append(j)

    return ans

