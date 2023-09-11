def findSubsetsThatSumToK(arr, n, k) :
    res = []

    def dfs(i, total, cur):
        if i == n:
            if total == k:
                res.append(cur)
            return

        dfs(i+1, total+arr[i], cur+[arr[i]])
        dfs(i+1, total, cur)

    dfs(0,0,[])
    return res

# def findSubsetsThatSumToK(arr, n, k) :
#     res = []

#     def dfs(i, cur, total):
#         if i == n:
#             if total == k:
#                 res.append(cur.copy())
#             return
        
#         cur.append(arr[i])
#         dfs(i+1, cur, total+arr[i])
#         cur.pop()
#         dfs(i+1, cur, total)
#     dfs(0, [], 0)
#     return res