"""
middle 2022-03-04 最小堆（堆里放高频的）
【heapq的使用方法+注意事项】
https://leetcode-cn.com/problems/top-k-frequent-elements/solution/347-qian-k-ge-gao-pin-yuan-su-zhi-jie-pa-wemd/
思路一：最简单粗暴的思路就是 使用排序算法对元素按照频率由高到低进行排序，然后再取前 k 个元素。
题目要求算法的时间复杂度必须优于O(nlogn)--【希尔、归并、快速、堆排】

维护一个元素数目为 k 的最小堆
每次都将新的元素与堆顶元素（堆中频率最小的元素）进行比较
如果新的元素的频率比堆顶端的元素大，则弹出堆顶端的元素，将新的元素添加进堆中
最终，堆中的 k 个元素即为前 k 个高频元素
"""
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        # 1. 构建元素-频率的对应关系，统计元素的频率
        hashmap = {}
        for x in nums:
            hashmap[x] = hashmap.get(x,0)+1
        # 2. 维护小顶堆
        heap  = [] # 默认第一个元素的小顶堆
        for ch,freq in hashmap.items():
            # print(ch,freq)
            if len(heap)>=k:
                if freq>heap[0][0]:
                    heapq.heapreplace(heap, (freq,ch))
            else:

                heapq.heappush(heap, (freq,ch))
        # heap中只存了k个元素，按照第一个元素升序排的
        # for x in heap:
        #     print(x)
        # (1, 3)
        # (2, 2)
        # (3, 1)
        return [item[1] for item in heap]
# """
#         import heapq
#         q = []
#         hashmap = Counter(nums)
#
#         for ch,freq in hashmap.items():
#             heapq.heappush(q, (freq,ch))
#             if len(q)>k:
#                 heapq.heappop(q)
#
#         return [x[1] for x in q]
# """
    # """
    # 快排
    # 时间复杂度：平均O(n)
    # 空间复杂度：O(n)
    # """
    # def topKFrequent(self, nums, k):
    #     count = collections.Counter(nums)
    #     num_cnt = list(count.items())
    #     print('count', count)
    #     print('num_cnt', num_cnt) # [(4, 1), (1, 1), (-1, 2), (2, 2), (3, 1)]
    #     topKs = self.findTopK(num_cnt, k, 0, len(num_cnt) - 1)
    #     return [item[0] for item in topKs]
    #
    # def findTopK(self, num_cnt, k, low, high):
    #     pivot = random.randint(low, high)
    #     num_cnt[low], num_cnt[pivot] = num_cnt[pivot], num_cnt[low]
    #     base = num_cnt[low][1]
    #     i = low
    #     for j in range(low + 1, high + 1):
    #         if num_cnt[j][1] > base:
    #             num_cnt[i + 1], num_cnt[j] = num_cnt[j], num_cnt[i + 1]
    #             i += 1
    #     num_cnt[low], num_cnt[i] = num_cnt[i], num_cnt[low]
    #     if i == k - 1:
    #         return num_cnt[:k]
    #     elif i > k - 1:
    #         return self.findTopK(num_cnt, k, low, i - 1)
    #     else:
    #         return self.findTopK(num_cnt, k, i + 1, high)

if __name__ == '__main__':
    # nums = [1, 1, 1, 2, 2, 3] # 1,2
    nums = [4,1,-1,2,-1,2,3] #[-1,2]
    k = 2 # 1,2
    print(Solution().topKFrequent(nums,k))