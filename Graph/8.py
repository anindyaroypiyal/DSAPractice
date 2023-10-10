def dfsCheck(node, vis, path_vis, adj):
    #when we encounter a node, we mark their path.
    vis[node] = True
    path_vis[node] = True

    #recursively check for the cycle.
    #if cycle is found it will be on the same path as visited.
    for ad in adj[node]:
        if (vis[ad] == False):
            if dfsCheck(ad, vis, path_vis, adj):
                return True
        elif path_vis[ad]:
            return True

    path_vis[node] = False
    return False

def detectCycleInDirectedGraph(n, edges):
    # Write your code here

    #make the adjacency list for storing the graph elements, here 1 based.
    adj = {i:[] for i in range(1,n+1)}
    for i in edges:
        u, v = i
        adj[u].append(v)

    # make visited and path visited array for keeping the check
    vis = [False]*(n+1)
    path_vis = [False]*(n+1)

    # check for the cycle using dfs
    for i in adj:
        if (vis[i] == False):
            
            if (dfsCheck(i, vis, path_vis, adj)):
                return 1
    return 0