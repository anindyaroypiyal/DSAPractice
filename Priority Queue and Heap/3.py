def getKthLargest(arr, k):
    ans=[]
    
    for i in range(len(arr)):
        Sum=0
        for j in range(i,len(arr)):
            Sum+=arr[j]
            ans.append(Sum)
    ans.sort()
#     ans=ans[::-1]
    return ans[len(ans)-k]