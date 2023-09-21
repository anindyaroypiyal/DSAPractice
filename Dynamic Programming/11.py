from sys import stdin
import sys
sys.setrecursionlimit(10**7) 
def editDistance(str1, str2) :
    
    # Your code goes here
    cache = [[float('inf')]*(len(str2)+1) for i in range(len(str1)+1)]
    
    for i in range(len(str1)+1):
        cache[i][len(str2)] = len(str1) - i
    for j in range(len(str2)+1):
        cache[len(str1)][j] = len(str2) - j
    
    for i in range(len(str1)-1,-1,-1):
        for j in range(len(str2)-1,-1,-1):
            if str1[i] == str2[j]:
                cache[i][j] = cache[i+1][j+1]
            else:
                cache[i][j] = 1 + min(cache[i+1][j], cache[i][j+1], cache[i+1][j+1])

    return cache[0][0]


























    
#taking inpit using fast I/O
def takeInput() :
    str1=input()
    str2=input()

    return str1, str2


#main
str1, str2  = takeInput()
print(editDistance(str1, str2))
