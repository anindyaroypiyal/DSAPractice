from os import *
from sys import *
from collections import *
from math import *

def ratInAMaze(maze, n):
    # Write your code here.
    visited = [[0]*n for i in range(n)]
    result = []
    helper(maze, n, 0, 0, visited, result)
    for i in range(len(result)):
        for j in range(len(result[0])):
            print(result[i][j], end=" ")
        print()
    return
    
    
def helper(maze, n, row, col, visited, result):
    #base case
    if row < 0 or row >= n or col < 0 or col >= n or maze[row][col] == 0 or visited[row][col] == 1:
        return
    
    if row == n-1 and col == n-1:
        visited[row][col] = 1
        path = []
        for i in range(n):
            for j in range(n):
                path.append(visited[i][j])
        result.append(path.copy())
    
    visited[row][col] = 1
    rowI = [0, -1, 0, 1]
    colJ = [-1, 0, 1, 0]
    for i in range(4):
        helper(maze, n, row+rowI[i], col+colJ[i], visited, result)
    visited[row][col] = 0

# Main.
n = int(input())
maze = n*[0]

for i in range(0 , n):
    maze[i]=input().split()
    maze[i]=[int(j) for j in maze[i]]
    
ratInAMaze(maze , n) 