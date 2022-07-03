"""
middle 2022-05-26 滑动窗口
https://leetcode.cn/problems/minimum-operations-to-reduce-x-to-zero/solution/hua-dong-chuang-kou-wen-ti-zhuan-hua-wei-vwwe/
求最长连续子数组的最长长度，使其和位sum(nums)-x
"""

class Solution:
    def minOperations(self, nums, x):
        pass

if __name__ == '__main__':
    nums = [1, 1, 4, 2, 3]
    x = 5
    print(Solution().minOperations(nums,x))