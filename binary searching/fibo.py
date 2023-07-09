def fibo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
print(fibo(6))

def towerOfHanoi(n, source, destination, aux):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    towerOfHanoi(n-1, source, aux, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    towerOfHanoi(n-1, aux, destination, source)

towerOfHanoi(3, 'A', 'C', 'B')

def nthTerm(n):
    if n == 1:
        return 1
    else:
        return nthTerm(n-1) + 2 * n - 1
    
print(nthTerm(4))
