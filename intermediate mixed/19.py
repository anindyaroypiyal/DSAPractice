from sys import stdin,setrecursionlimit
from queue import Queue

setrecursionlimit(10**7)

# Binary tree node class for reference.
class BinaryTreeNode :
	def __init__(self, data) :
		self.data = data
		self.left = None
		self.right = None



def parent_make(parent, root, start):
    target = None
    q = [root]
    while q:
        f = q.pop(0)
        if f.data == start:
            target = f
        if f.left:
            q.append(f.left)
            parent[f.left] = f
        if f.right:
            q.append(f.right)
            parent[f.right] = f
    return target

def timeToBurnTree(root, start):
    parent = {}
    target = parent_make(parent, root, start)
    q = [target]
    burn = {target: True}
    cnt = 0

    while q:
        s = len(q)
        fl = 0

        for i in range(s):
            temp = q.pop(0)
            
            if temp.left and not burn.get(temp.left, False): #dictionay .get(key== required, value== optional, A value to return if the specified key does not exist.)
                q.append(temp.left)
                burn[temp.left] = True
                fl = 1

            if temp.right and not burn.get(temp.right, False):
                q.append(temp.right)
                burn[temp.right] = True
                fl = 1

            if parent.get(temp) and not burn.get(parent[temp], False):
                q.append(parent[temp])
                burn[parent[temp]] = True
                fl = 1

        if fl:
            cnt += 1

    return cnt



















# Fast input
def takeInput() :
	
    arr = list(map(int, stdin.readline().strip().split(" ")))

    rootData = arr[0]

    n = len(arr)

    if(rootData == -1) :
        start = int(input().strip())
        return None, start

    root = BinaryTreeNode(rootData)
    q = Queue()
    q.put(root)
    index = 1
    while(q.qsize() > 0) :
        currentNode = q.get()  
        
        leftChild = arr[index]
        
        if(leftChild != -1) :
            leftNode =  BinaryTreeNode(leftChild)  
            currentNode.left = leftNode  
            q.put(leftNode)  
        
        index += 1
        rightChild = arr[index]
        
        if(rightChild != -1) :
            rightNode = BinaryTreeNode(rightChild)
            currentNode .right = rightNode  
            q.put(rightNode)  

        index += 1

    start = int(input().strip())

    return root, start

#main

root, start = takeInput()

print(timeToBurnTree(root, start))