from typing import List

class Disjoint:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.size = [1] * (n+1)
    
    def findParent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    
    def unionBySize(self, u, v):
        pu = self.findParent(u)
        pv = self.findParent(v)
        if self.size[pu] < self.size[pv]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]

def isValid(adjR, adjC, n, m):
    return adjR >=0 and adjR < n and adjC >= 0 and adjC < m


def numberOfIslandII(n: int, m: int, queries: List[List[int]], q: int)-> int:
    # Write your code here.
    ds = Disjoint(n*m)
    vis = [[0]*m for i in range(n)]
    
    count = 0
    ans = []

    for row,col in queries:
        if vis[row][col] == 1:
            ans.append(count)
            continue
        vis[row][col] = 1
        count+=1

        dr = [-1,0,1,0]
        dc = [0,1,0,-1]

        for i in range(4):
            adjR = row + dr[i]
            adjC = col + dc[i]

            if (isValid(adjR, adjC, n, m)) and (vis[adjR][adjC]==1):
                nodeNo = row * m + col
                adjNodeNo = adjR * m + adjC

                if (ds.findParent(nodeNo) != ds.findParent(adjNodeNo)):
                    count -= 1
                    ds.unionBySize(nodeNo, adjNodeNo)
        ans.append(count)
    return ans