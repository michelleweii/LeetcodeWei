"""
middle 2021-08-19 dp 01背包
（优化前）f[i][j]为从 nums 凑出总和「恰好」为 j 的方案数。
（优化后）dp[i] 表示和为 i 的 num 组合有 dp[i] 种。
感觉求所有方案数基本都是dp[i] = dp[i]+dp[i-num]
求torf，dp[i] = dp[i] OR dp[i-num]
"""
# 两个连接结合看
# (优化)https://leetcode-cn.com/problems/coin-change/solution/yi-tao-kuang-jia-jie-jue-bei-bao-wen-ti-h0y40/
# (未优化)https://leetcode-cn.com/problems/target-sum/solution/gong-shui-san-xie-yi-ti-si-jie-dfs-ji-yi-et5b/
# 数学知识：
# 我们想要的 target = 正数和 - 负数和 = x - y
# 已知 x 与 y 的和是数组总和：x + y = sum
# 可以求出 x = (target + sum) / 2 # 令『正值部分』的绝对值总和为x。
# 问题转换为：只使用 + 运算符，从 nums 凑出 x 的方案数。
class Solution:
    def findTargetSumWays(self, nums, target):
        sums = sum(nums)
        if target>sums or (sums + target) % 2 == 1: return 0
        positive = (target+sums)//2
        dp = [0]*(positive+1) # 表示和为 i 的 num 组合有 dp[i] 种。
        dp[0] = 1 # 表示只有当不选取任何元素时，元素之和才为 0，因此只有 1 种方案。
        for num in nums:
            for i in range(positive, num-1, -1):
                # f[i][j]=f[i−1][j]+f[i−1][j+nums[i−1]]
                dp[i] = dp[i] + dp[i-num] # i >= num
                # dp[i] 不选
                # dp[i-num] 选
        return dp[positive]

if __name__ == '__main__':
    # nums = [1, 1, 1, 1, 1]
    # s = 3
    # (sums + target) % 2 == 1: return 0 专门针对以下情况
    nums = [7, 9, 3, 8, 0, 2, 4, 8, 3, 9]
    s = 0
    # 0
    print(Solution().findTargetSumWays(nums,s))
