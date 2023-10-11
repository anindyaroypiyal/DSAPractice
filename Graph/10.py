
def dfs(node, color_val, color_list, edges):
    color[node] = color_val
    for u in range(v):
        if (edges[node][u] == 1) and (color[u] == -1):
            if (dfs(u), 1 - color_val, color_list, edges) == False:
                return False
        elif (color[u] == color_val):
            return False
    return True
         

def isGraphBirpartite(edges):
    #Write your code here.
    v = len(edges)
    color = (-1) * v

    for i in range(v):
        if (color[i] == -1) and (dfs(i, 0, color, edges) == False):
            return False
    return True
