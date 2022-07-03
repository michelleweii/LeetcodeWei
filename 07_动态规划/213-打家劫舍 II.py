"""
middle 2021-12-07 dp （2020秋招pdd）
基础题198，进阶版：这个地方所有的房屋都 “围成一圈” ，这意味着第一个房屋和最后一个房屋是紧挨着的。
dp[i] 代表前 i 个房子在满足条件下的能偷窃到的最高金额。
https://leetcode-cn.com/problems/house-robber-ii/solution/213-da-jia-jie-she-iidong-tai-gui-hua-jie-gou-hua-/
"""
#         转化成2个打家劫舍
#         /*分析：依然使用动态规划,只不过最后一个元素需要特殊处理
#         * 核心：第一个元素与最后一个元素,只能取一个--->分解成两问题*/
#         // 遍历dp --> 不用最后一个元素
#         // 遍历dp --> 不用第一个元素

# /*
# 环状排列意味着第一个房子和最后一个房子中只能选择一个偷窃，
# 因此可以把此环状排列房间问题约化为两个单排排列房间子问题(198)：
# 在不偷窃第一个房子的情况下（即 nums[1:]），最大金额是p1；
# 在不偷窃最后一个房子的情况下（即 nums[:n-1]），最大金额是p2。
# 综合偷窃最大金额： 为以上两种情况的较大值，即 max(p1,p2)。
# */

class Solution:
    def rob(self, nums):
        n = len(nums)
        if n==0:return 0
        if n==1:return nums[0]
        res1 = self.rob_range(nums, 0, n-2) # 遍历dp --> 不用最后一个元素
        res2 = self.rob_range(nums, 1, n-1) # 遍历dp --> 不用第一个元素
        return max(res1,res2)

    # lc198
    def rob_range(self, nums, start, end):
        if start==end:return nums[start]
        dp = [0]*len(nums)
        dp[start] = nums[start]
        dp[start+1] = max(nums[start], nums[start+1])
        for i in range(start+2, end+1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i]) # 不选第i个屋子，选第i个屋子

        return dp[end] # dp[-1]


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(Solution().rob(nums))