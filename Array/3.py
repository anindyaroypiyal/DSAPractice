def rotateArray(arr: list, k: int) -> list:
    # Write your code here.
    length = len(arr)
    rev(arr,0,length-1)
    rev(arr, length-k, length-1) #reversing last k element.
    rev(arr, 0, length-k-1) #reversing remaining. length - k - 1, becasue k is 1 based.

    return arr

def rev(arr, l, r): #reverse function.
    while l<r:
        arr[l],arr[r] = arr[r],arr[l]
        l,r = l+1, r-1
    return
 
# 2 methods for solving this problem:
# o(n) method: use a new array, copy from main array, use % operation.

# o(1) method: all operation in place.
# reverse the main array,
# reverse first k elements, (for right rotate)
#reverser the last k elements, (for left rotate)
# reverse the remaining elements.