import heapq
def kthSmallLarge(arr, n, k):
    # Write your code here
    
    b = heapq.nlargest(k, arr)
    a = heapq.nsmallest(k, arr)
    return [a[k-1],b[k-1]]
    