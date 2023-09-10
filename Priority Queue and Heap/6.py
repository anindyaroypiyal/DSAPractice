from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)
import heapq

def connectRopes( arr, n) :

	# Your code goes here
	ans = []

	heapq.heapify(arr)

	while len(arr) != 1:
		a = heapq.heappop(arr)
		b = heapq.heappop(arr)

		ans.append(a+b)
		if len(arr) == 0:
			break
		heapq.heappush(arr, (a+b))

	return (sum(ans))































#taking inpit using fast I/O
def takeInput() :
	n = int(input())

	if n == 0 :
		return list(), 0

	arr = list(map(int, stdin.readline().strip().split(" ")))

	return arr, n


#main
arr, n = takeInput()
print(connectRopes( arr, n))
