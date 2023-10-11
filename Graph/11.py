from os import *
from sys import *
from collections import *
from math import *

def bellmonFord(n, m, src, dest, edges):
    # Write your code here.

    dist = [1e8]*n
    dist[src] = 0

    for i in range(n-1):
        for u,v,w in edges:
            if (dist[u] != 1e8) and (dist[u] + w < dist[v]):
                dist[v] = dist[u] + w

    # nth relaxation for detecting negative cycle, if the dist list changes further that means there is a negative cycle.
    for u,v,w in edges:
            if (dist[u] != 1e8) and (dist[u] + w < dist[v]):
                return {-1}

    return dist
 


