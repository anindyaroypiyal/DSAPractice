# 3 steps:
# 1) move n-1 from source, using destination, to aux
# 2) move last 1 from source to destination
# 3) move back the n - 1 from aux, using source, to destination


def toh(n,source,auxiliary,destination,ans):
    if n==0:
        return
    toh(n - 1, source, destination, auxiliary, ans)
    ans.append([source, destination])
    toh(n - 1, auxiliary, source, destination, ans)


def towerOfHanoi(n):
    # Write your code here
    # Return a 2-D array
    ans = []    
    toh(n,1,2,3,ans)    
    return ans  
