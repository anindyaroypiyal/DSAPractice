def search(arr, target) :
    # Write your code here.
    lo = 0
    hi = len(arr) - 1

    while (lo <= hi):
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
    
    # left sorted portion
        if arr[lo] <= arr[mid]:
            if (target > arr[mid] or target < arr[lo]):
                lo = mid + 1
            else:
                hi = mid - 1
    
    # right sorted portion
        else:
            if (target < arr[mid] or target > arr[hi]):
                hi = mid - 1
            else:
                lo = mid + 1
    return -1