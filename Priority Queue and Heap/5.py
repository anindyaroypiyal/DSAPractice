import heapq
import statistics
import math

def findMedian(arr, n):
    # Write your code here
    heap = []
    ans = []
    heapq.heapify(heap)

    for i in range(n):
        heapq.heappush(heap, arr[i])
        ans.append(math.floor(statistics.median(heap)))

    for i in ans:
        print(i,end=' ')

    # min_heap = []
    # heapq.heapify(min_heap)

    # max_heap = []
    # heapq._heapify_max(max_heap)

    # ans = []

    # for i in range(n):
    #     if len(max_heap) == 0 or max_heap[0] >= arr[i]:
    #         heapq.heappush(max_heap, arr[i])
    #         # heapq.heapify(max_heap)
    #     else:
    #         heapq.heappush(min_heap, arr[i])

    #     if len(max_heap) > (len(min_heap)+1):
    #         heapq.heappush(min_heap, heapq._heappop_max(max_heap))
    #     elif len(max_heap) < len(min_heap):
    #         heapq.heappush(max_heap, heapq.heappop(min_heap))
    #         # heapq.heapify(max_heap)

    #     print(min_heap, 'min')
    #     print(max_heap, 'max')

    #     if len(min_heap) == len(max_heap):
    #         temp = (min_heap[0] + max_heap[0]) // 2
    #         ans.append(math.floor(temp))
    #     else:
    #         ans.append(math.floor(max_heap[0]))

    # print(ans)
    # return []