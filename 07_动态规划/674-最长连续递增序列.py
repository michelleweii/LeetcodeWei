"""
easy 2022-02-23 dp
# 与LC300的区别，本题是连续
状态定义：dp[i]表示以nums[i-1]为结尾的最长连续递增子序列个数【nums[i]必有】
状态转移：因为必须要连续，所以要构成递增关系 dp[i] = dp[i-1]+1 if nums[i]>nums[i-1]
LC300：dp[i] = max(dp[i], dp[j] + 1) for j in [0, i)
"""
# https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence/solution/tu-biao-si-lu-kan-bu-dong-ni-da-wo-ji-ba-7fr7/
class Solution:
    def findLengthOfLCIS(self, nums):
        if not nums:return 0
        n = len(nums)
        dp = [1]*n
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                dp[i] = dp[i-1]+1

        return max(dp)


if __name__ == '__main__':
    nums = [1,3,5,4,7]
    print(Solution().findLengthOfLCIS(nums))
    # 3
    # 解释：最长连续递增序列是 [1,3,5], 长度为3。
    # 尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为 5 和 7 在原数组里被 4 隔开。