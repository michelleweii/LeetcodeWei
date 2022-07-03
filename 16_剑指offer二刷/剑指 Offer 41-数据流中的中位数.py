"""
hard 堆排序
2021-07-26
https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/solution/mian-shi-ti-41-shu-ju-liu-zhong-de-zhong-wei-shu-y/
"""
# Python 中 heapq 模块是小顶堆。实现 大顶堆 方法： 小顶堆的插入和弹出操作均将元素 取反 即可。
from heapq import *
class MedianFinder:
    def __init__(self):
        self.small_heap = [] # 小顶堆，保存较大的一半(插正数)
        self.big_heap = [] # 大顶堆，保存较小的一半(插负数)

    def addNum(self, num: int):
        # 当两堆不同，奇数
        # 需向 big_heap 添加一个元素。实现方法：将新元素 num 插入至 small_heap,
        # 再将 small_heap 堆顶元素插入至 big_heap ；
        if len(self.small_heap) != len(self.big_heap):
            heappush(self.small_heap, num)
            heappush(self.big_heap, -heappop(self.small_heap))
        # 当两堆相同，偶数
        # 需向 small_heap 添加一个元素。实现方法：将新元素 num 插入至 big_heap,
        # 再将 big_heap 堆顶元素插入至 small_heap ；
        else:
            heappush(self.big_heap, -num)
            heappush(self.small_heap, -heappop(self.big_heap))
        # print(self.small_heap)


    def findMedian(self) -> float:
        if len(self.small_heap) != len(self.big_heap):
            return self.small_heap[0]
        # print(self.small_heap[0])
        # print(self.big_heap[0]) # 大顶堆出来的元素是负数
        return (self.small_heap[0]-self.big_heap[0])/2.0


if __name__ == '__main__':
    obj = MedianFinder()
    nums = [1,2,3,4,5]
    for num in nums:
        obj.addNum(num)

    param_2 = obj.findMedian()
    print(param_2)