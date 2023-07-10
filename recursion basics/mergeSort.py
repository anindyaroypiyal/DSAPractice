def mergeSort(arr, n):
    # Write your code here.
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid], n)
    right = mergeSort(arr[mid:], n)
    return merge(left, right)
    

def merge(left, right):
    res = []
    i,j = 0,0

    while i < len(left) and j < len(right):
        if left[i] <=  right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res += left[i:]
    res += right[j:]
    return res

