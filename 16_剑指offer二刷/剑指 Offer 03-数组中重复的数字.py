"""
原地置换 easy
哈希表更容易理解
https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/solution/yuan-di-jiao-huan-yi-jiao-huan-luo-bu-bi-gh5c/
"""
class Solution:
    def findRepeatNumber(self, nums):
        """
        n = len(nums)
        for i in range(n):
            while nums[i]!=i and nums[nums[i]]!=nums[i]:
                # print(i, nums[i], nums[nums[i]])
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
                # print(i, nums) # python nums出了while循环就恢复原样了！
                if nums[i] != nums[nums[i]] and nums[nums[i]]==nums[i]:
                    return nums[i]
        return -1
        """
        n = len(nums)
        for i in range(n):
            while nums[i] != i:
                if nums[nums[i]] == nums[i]: return nums[i]
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1


if __name__ == '__main__':
    nums = [2, 3, 1, 0, 2, 5, 3]
    print(Solution().findRepeatNumber(nums))