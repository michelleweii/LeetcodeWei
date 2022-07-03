# -*- coding:utf-8 -*-
import heapq
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # 维护一个大顶堆
        # 将列表转为堆
        heapt = []
        for item in tinput:
            heapq.heappush(heapt,item)
        res = heapq.nsmallest(k,heapt)
        print(res)


if __name__ == '__main__':
    tinput = [4,5,1,6,2,7,3,8]
    k = 4
    Solution().GetLeastNumbers_Solution(tinput,k)


