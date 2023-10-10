from os import *
from sys import *
from collections import *
from math import *

def dfs(node, graph, visited, stack):
    # Append child before parent for all vertices
    visited[node] = True
    for adjNode in graph[node]:
        if not visited[adjNode]:
            dfs(adjNode, graph, visited, stack)
    stack.append(node)


def topologicalSort(adj, v, e):
    # create adjacency list from edges pair
    graph = [[] for _ in range(v)]
    for i in range(e):
        u, v = adj[i]
        graph[u].append(v)
    
    # coz passed v is incorrect
    v = len(graph)

    visited = [False] * v
    stack = []

    # DFS approach
    for i in range(v):
        if not visited[i]:
            dfs(i, graph, visited, stack)
    
    res = []
    while(stack):
        res.append(stack.pop())

    return res