"""
middle 2021-12-08 超级常考
!!!要求连续 一维dp
https://leetcode-cn.com/problems/maximum-product-subarray/solution/dpfang-fa-xiang-jie-by-yang-cong-12/
- 数组：要求连续i-1,i,i+1
- 子序列：不要求连续i-3,i,i+5
"""
# 题目：给定一个整数数组nums，找出一个序列中乘积最大的连续子数组（该序列至少包含一个数）。
# 思路：需要维护两个变量，当前的最大值，以及最小值，最小值可能为负数，
# 但没准下一步乘以一个负数，当前的最大值就变成最小值，而最小值则变成最大值了
# 注意元素为0的情况，如果A[i]为0，那么maxDP和minDP都为0，我们需要从A[i + 1]重新开始。

# 状态定义：两个DP分别定义为【以i结尾的子数组】的最大积与最小积；
class Solution:
    def maxProduct(self, nums):
        n = len(nums)
        if n==0:return 0
        res = nums[0] # 答案

        # 状态定义：两个mDP分别定义为以i结尾的子数组的最大积与最小积；
        max_dp, min_dp = [0] * n, [0] * n
        # 初始化dp
        max_dp[0], min_dp[0] = nums[0], nums[0]

        #  //最大积的可能情况有：元素i自己本身，上一个最大积与i元素累乘，上一个最小积与i元素累乘；
        #  //与i元素自己进行比较是为了处理i元素之前全都是0的情况；
        for i in range(1,n):
            max_dp[i] = max(nums[i], max_dp[i-1]*nums[i], min_dp[i-1]*nums[i])
            min_dp[i] = min(nums[i], max_dp[i-1]*nums[i], min_dp[i-1]*nums[i])
        #  //记录ans；
            res = max(res, max_dp[i])

        return res

if __name__ == '__main__':
    nums = [2,3,-2,4]
    print(Solution().maxProduct(nums))