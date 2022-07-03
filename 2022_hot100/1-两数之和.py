"""
easy 2022-01-04 哈希表
https://www.bilibili.com/video/BV1Lb411w74Y
要求时间复杂度O(N)
"""
# k: target-num
# v: num index
class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return [hashmap[nums[i]], i]
            else:
                hashmap[target - nums[i]] = i

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums,target))