def NthRoot(n: int, m: int) -> int:

    l = 1

    r = m

    while l <= r:

        mid = l+(r-l)//2

        if mid ** n == m:

            return int(mid)

        elif mid ** n > m:

            r = mid-1 

        else:

            l = mid+1


    return -1