import collections
def maxSlidingWindow(arr, n, k):
    # Write your code here.
    # i,j = 0,0
    # ans = []
    # tr = []
    # while (j<n):
    #     tr.append(arr[j])
    #     j+=1

    #     if (j-i) < k:
    #         continue
    #     if (j-i) == k:
    #         ans.append(max(tr))
    #         tr.remove(arr[i])
    #     i+=1
    # return ans
    #it works but brute force: repetitive work


    output = []
    q = collections.deque() #index
    l = r = 0

    while r<n:
        #pop smaller values from q
        while q and arr[q[-1]] < arr[r]:
            q.pop()
        q.append(r)

        r+=1

        #remove left value from window
        if l > q[0]:
            q.popleft()

        if (r - l) >= k:
            output.append(arr[q[0]])
            l+=1
            
    return output