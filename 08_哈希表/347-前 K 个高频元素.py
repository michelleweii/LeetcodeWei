"""
middle
哈希表+小顶堆
key: 元素
value: 出现的个数
"""
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        hash_map = {}
        for x in nums:
            hash_map[x] = hash_map.get(x,0)+1

        # s = []
        # for p in hash_map:
        #     s.append(hash_map[p])
        # print("s:", s) # s: [3, 2, 1]
        #

        # 构建小顶堆
        p = []
        for keys,v in hash_map.items():
            heapq.heappush(p, (v, keys))

        return [i[1] for i in heapq.nlargest(k,p)]

if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    res = Solution()
    print(res.topKFrequent(nums,k))