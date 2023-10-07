from os import *
from sys import *
from collections import *
from math import *
import heapq

def dijkstra(vec, vertices, edges, source):
    # Write your code here.
    adj = {}
    for i in range(vertices):
        adj[i] = []

    for s, d, w in vec:
        adj[s].append([d,w])
        adj[d].append([s,w])

    shortest = {}
    minHeap=[[0,source]]
    while minHeap:
        w1, n1 = heapq.heappop(minHeap)
        if n1 in shortest:
            continue
        
        shortest[n1] = w1

        for n2, w2 in adj[n1]:
            if n2 not in shortest:
                heapq.heappush(minHeap, [w1+w2, n2])

    for i in range(vertices):
        if i not in shortest:
            shortest[i] = 2147483647
        
    return [shortest[i] for i in shortest]
    
# def dijkstra(vec, vertices, edges, source):
#     # Write your code here.
#     adj = [[] for i in range(vertices)]
#     for s,e,w in vec:
#         adj[s].append([e,w])
#         adj[e].append([s,w])

#     dis = [2147483647 for i in range(vertices)]
#     dis[source] = 0
#     q = [0]
#     while q:
#         node = q.pop(0)
#         for adjnode, wt in adj[node]:
#             if dis[node]+wt<dis[adjnode]:
#                 dis[adjnode] = dis[node]+wt
#                 q.append(adjnode)
#     return dis
