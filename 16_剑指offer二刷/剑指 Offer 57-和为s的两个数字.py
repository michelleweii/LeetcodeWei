"""
easy hashmap
2021-07-19
"""
class Solution:
    def twoSum(self, nums, target):
        if not nums:return []
        hashmap = {}
        for x in nums:
            # print(hashmap)
            if hashmap.get(x,0):return [x, hashmap[x]]
            hashmap[target-x] = x
        return []

if __name__ == '__main__':
    nums = [10, 26, 30, 31, 47, 60]
    target = 40
    print(Solution().twoSum(nums, target))