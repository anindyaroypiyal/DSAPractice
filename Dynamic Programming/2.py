from sys import stdin

def maxMoneyLooted(houses, n) :
    #Your code goes here
    rob1, rob2 = 0,0

    for i in houses:
        temp = max(i+rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2 





























#taking input using fast I/O method

def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#main
arr, n = takeInput()
print(maxMoneyLooted(arr, n))