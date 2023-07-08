def singleNonDuplicate(arr):
    # Write your code here
    if len(arr) == 1:
        return arr[0]
    elif arr[0] != arr[1]:
        return arr[0]
    elif arr[-1] != arr[-2]:
        return arr[-1]
    
    lo = 1
    hi = len(arr) - 2
    while(lo <= hi):
        mid = lo + ((hi-lo)//2)

        if (arr[mid] != arr[mid+1] != arr[mid-1]):
            return arr[mid]
        if (((arr[mid] == arr[mid-1]) and (mid%2 != 1)) or ((arr[mid]==arr[mid+1]) and (mid%2 == 0))):
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
