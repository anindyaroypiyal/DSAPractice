def canPartition(arr, n):
    # Write your code here.
    if sum(arr) % 2:
        return False
    
    target = sum(arr) // 2
    dp = set()
    dp.add(0)

    for i in range(n-1,-1,-1):
        nextDp = set()

        for t in dp:
            if (t+arr[i]) == target:
                return True
            nextDp.add(t+arr[i])
            nextDp.add(t)
        dp = nextDp
    return False