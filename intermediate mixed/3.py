import queue
import sys

class BinaryTreeNode:
    
    def __init__(self, data):
        
        self.data = data
        self.left = None
        self.right = None

def lca(root, node1, node2, node3):
    if not root:
        return None
    
    if root.data == node1 or root.data == node2 or root.data == node3:
        return root
    

    l = lca(root.left,node1, node2, node3)
    r = lca(root.right,node1, node2, node3)

    if l and r:
        return root
    else:
        return l or r


def lcaOfThreeNodes(root, node1, node2, node3):
    
    # Write your code here.
    sys.setrecursionlimit(10**7)            # take care
    par=lca(root,node1,node2,node3)
    return par.data


# Building the tree.
def buildLevelTree(levelorder):
    
    index = 0
    length = len(levelorder)
    
    if length<=0 or levelorder[0]==-1:
        return None
    
    
    root = BinaryTreeNode(levelorder[index])
    index += 1
    
    q = queue.Queue()
    q.put(root)
    
    while not q.empty():
        
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        
        if leftChild != -1:
            
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
            
        rightChild = levelorder[index]
        index += 1
        
        
        if rightChild != -1:
            
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
            
            
    return root
    
t = int(input())
while t > 0:
    arr = [int(i) for i in input().split()][:3]
    li = [int(i) for i in input().split()]
    root = buildLevelTree(li)
    print(lcaOfThreeNodes(root, arr[0], arr[1], arr[2]))
    t = t - 1