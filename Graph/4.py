from os import *
from sys import *
from collections import *
from math import *

import heapq

def calculatePrimsMST(n, m, g):
    # Write your code here.
    # Return a 2-D list.
    adj = {i:[] for i in range(n+1)}

    for src, des, wt in g:
        adj[src].append((des, wt))
        adj[des].append((src, wt))

    minHeap = [(0,1,-1)]  #weight, destination, parent
    vis = [False for i in range(n+1)]
    ans = []
    # min_sum = 0

    while minHeap:
        weight, node, parent = heapq.heappop(minHeap)
        if vis[node] == True:
            continue
        
        vis[node] = True
        # min_sum += weight
        if parent != -1:
            ans.append([parent, node, weight])
        
        for dest,weight in adj[node]:
            if vis[dest]==False:
                heapq.heappush(minHeap, (weight, dest, node))

    return ans