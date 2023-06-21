n = 6
arr = [10,20,-30,40,-50,60]
sum = 0
max_sum = 0
for i in range(n):
    sum = sum + arr[i]
    if sum < 0:
        sum = 0
    max_sum = max(sum, max_sum)
    # return the answer
print(max_sum)