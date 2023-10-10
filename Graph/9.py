from typing import *

def graphColoring(mat: List[List[int]], m: int) -> str:

    v = len(mat)

    color = [-1]*v

 

    def issafe(vert, c):

        for u in range(v):

            if mat[vert][u] == 1 and color[u] == c:

                return False

        return True

 

    def graph_color_util(vert):

        if vert == v:

            return True

 

        for c in range(m):

            if issafe(vert, c):

                color[vert] = c

                if graph_color_util(vert + 1):

                    return True

                color[vert] = -1

 

    if not graph_color_util(0):

        return "NO"

    return "YES"

