def pushZerosAtEnd(arr):
    # write your code here
    # new_arr = []

    # count_0 = 0

    # for i in arr:
    #     if i != 0:
    #         new_arr.append(i)
    #     else:
    #         count_0 += 1
    
    # for i in range(count_0):
    #     new_arr.append(0)

    # arr = new_arr
    # print(arr)

    i = 0
    j = 0
    while(j < len(arr)):
        if(arr[j] != 0):
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            j+=1
        else:
            j+=1
    