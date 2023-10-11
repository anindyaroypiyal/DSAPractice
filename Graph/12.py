def floydWarshall(n, m, src, dest, edges):
    # Create adjacency matrix
    adj = [[0] * n for _ in range(n)]
    for x in edges:
        u, v, w = x
        adj[u - 1][v - 1] = w

    # Initialize unreachable paths with infinity
    for i in range(n):
        for j in range(n):
            if adj[i][j] == 0 and i != j:
                adj[i][j] = int(1e9)

    # Perform Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if adj[i][k] == int(1e9) or adj[k][j] == int(1e9):
                    continue
                adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])

    # Return shortest distance from source to destination
    return adj[src - 1][dest - 1]