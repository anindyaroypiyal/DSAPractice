
from sys import stdin


def minHeapToMaxHeap(arr, n) :
    #Write your code from here
    convertMaxHeap(arr, n)

def MaxHeapify(arr, i, N):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i
    if l < N and arr[l] > arr[i]:
        largest = l
    if r < N and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        MaxHeapify(arr, largest, N)
 
# This function basically builds max heap
 
 
def convertMaxHeap(arr, N):
 
    # Start from bottommost and rightmost
    # internal node and heapify all
    # internal nodes in bottom up way
    for i in range(int((N - 2) / 2), -1, -1):
        MaxHeapify(arr, i, N)
 
# A utility function to print a
# given array of given size
 
def printArray(arr, size):
    for i in range(size):
        print(arr[i], end=" ")
    print()







































'''----------utility functions for internal use----------'''
def isPermutation(inputArray, outputArray, n): 
    freq = dict()
    
    for num in inputArray :
        if num in freq :
            value = freq[num]
            freq[num] = value + 1
        else :
            freq[num] = 1
            
            
    for num in outputArray :
        if num in freq :
            value = freq[num]
            freq[num] = value - 1
            if freq[num] == 0 :
                del freq[num]
                
                
    return len(freq) == 0


def isMaxHeap(arr, index, n) :
    if (2 * index + 1) >= n :
        return True
        

    if (2 * index + 2) >= n :
        return (arr[index] >= arr[2 * index + 1]) and isMaxHeap(arr, 2 * index + 1, n)
    

    if (arr[index] >= arr[2 * index + 1]) and (arr[index] >= arr[2 * index + 2]) and isMaxHeap(arr, 2 * index + 1, n) and isMaxHeap(arr, 2 * index + 2, n) :
        return True

    return False


#taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))

    return arr, n


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    arr, n = takeInput()
    toValidate = arr[ : ]

    minHeapToMaxHeap(arr, n)

    if isPermutation(toValidate, arr, n) and isMaxHeap(arr, 0, n) :
        print("true")
    else :
        print("false")

    t -= 1