import math
def maxSubarraySum(arr, n):
	# Write your code here.

	max_sum = min(arr)
	cur_sum = 0
	max_arr = []

	l = len(arr)
	j=0

	for i in range(l):
		count = 0
		j = i
		max_sum = min(arr)
		cur_sum = 0
		while(count < l):
			cur_sum += arr[j%l]
			max_sum = max(max_sum, cur_sum)
			if cur_sum < 0:
				cur_sum = 0		
			j+=1
			count+=1
		max_arr.append(max_sum)
	return max(max_arr)