# -*- coding:utf-8 -*-
# 我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数
from heapq import *
class Solution:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
    def Insert(self, num):
        # 初始，一直向大顶堆中添加元素
        # 由于只能建立小根堆，所以大根堆采用添加负数的方法
        heappush(self.max_heap,-num)
        if (self.min_heap and (-self.max_heap[0]>self.min_heap[0])):
            maxv = -self.max_heap[0]
            minv = self.min_heap[0]
            heappop(self.max_heap[0]),heappop(self.min_heap[0])
            heappush(self.max_heap,-minv),heappush(self.min_heap,maxv)
        if len(self.max_heap)>(len(self.min_heap)+1):
            heappush(self.min_heap,-self.max_heap[0])
            heappop(-self.max_heap[0])
        print(self.min_heap)
        print(self.max_heap)

    def GetMedian(self):
        if (len(self.max_heap)+len(self.min_heap))&1: # 奇数
            mid = self.min_heap[0]
        else: # 偶数
            mid = (self.min_heap.pop()-self.max_heap.pop())/2.0
        return mid

if __name__ == '__main__':
    s = [1,2,3,4,5]
    for x in s:
        print(Solution().Insert(x))
    print(Solution().GetMedian())


