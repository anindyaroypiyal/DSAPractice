from os import *
from sys import *
from collections import *
from math import *

from collections import deque

def findShortestPath(matrix, sourceX, sourceY, destX, destY, n, m):
    # Extra space can be avoided by marking the visited 1's with 0's
    q = deque([(sourceX, sourceY, 0)])
    vis = set((sourceX, sourceY))

    while q:
        currX, currY, distance = q.popleft()
        
        if currX == destX and currY == destY:
            return distance + 1

        for dx, dy in [(-1,0),(0,1),(1,0),(0,-1)]:
            newX, newY = currX + dx, currY + dy

            if (newX >= 0 and newX < n and
            newY >= 0 and newY < m and
            (newX,newY) not in vis and
            matrix[newX][newY]):

                vis.add((newX,newY))
                q.append([newX,newY, distance+1])
    return -1


