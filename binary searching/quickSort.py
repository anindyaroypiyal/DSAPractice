def quickSort(arr):
    # Write the function here.
    _quickSort(arr, 0, len(arr)-1)
    print(arr)
    # return arr
    

def ppartition(a, start, end):
    i = start
    j = end - 1
    pivot = a[end]

    while i < j:
        while i < j and a[i] < pivot:
            i += 1
        while i < j and a[j] > pivot:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]

    if a[i] > pivot:
        a[i] , a[pivot] = a[pivot], a[i]

    return i

def _quickSort(arr, start, end):
    if start < end:
        partition = ppartition(arr, start, end)
        _quickSort(arr, start, partition-1)
        _quickSort(arr, partition+1, end)


a = [4, 2, 1, 3, 5, 7, 6, 8]
quickSort(a)