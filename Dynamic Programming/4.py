def minimumJumps(nums, n):
        l=r=0
        cnt=0
        idx=0
        while r<n-1:
            farthest=0
            for i in range(l,r+1):
                farthest=max(farthest,i+nums[i])
            l=r+1
            r=farthest
            cnt+=1
            idx+=1
            if idx>n:
                return -1

        return cnt