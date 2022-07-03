import heapq
q = []
# 实现小顶堆，优先队列默认使用小顶堆
heapq.heappush(q,1)
heapq.heappush(q,100)
heapq.heappush(q,66)
heapq.heappush(q,12)
print(q[0]) # 1
print(len(q)) # 4
print(q) # [1, 12, 66, 100],说明此时没有排序
print(heapq.heapify(q)) # None
# 从堆中删除元素，返回值是最小的
print(heapq.heappop(q)) # 1
print(q) # [12, 100, 66]
print(heapq.heappop(q)) # 12
print(q) # [66, 100]b
# 每次pop都是最小的元素，如何实现大顶堆，返回最大的元素呢
b = []
heapq.heappush(b,-1)
heapq.heappush(b,-100)
heapq.heappush(b,-66)
heapq.heappush(b,-12)
heapq.heappush(b,-200)
print(b) # [-200, -100, -66, -1, -12]
print(-heapq.heappop(b)) # 200
print(-heapq.heappop(b)) # 100
print(-heapq.heappop(b)) # 66
print(-heapq.heappop(b)) # 12