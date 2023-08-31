def nextGreater(S):
    # Write your code here
    # Return a string representing the next greater number of S
    l = list(map(int, S))
    ng(l)

def ng(l):
    n = len(l)

    for i in range(n-2, -1, -1):
        if l[i] < l[i+1]:
            break
    
    for j in range(n-1, i, -1):
        if l[i] < l[j]:
            break
    
    l[i], l[j] = l[j], l[i]

    l[i+1:] = reversed(l[i+1:])

    x=0
    for k in range(n):
        x = x*10 + l[k]
    
    print(x)