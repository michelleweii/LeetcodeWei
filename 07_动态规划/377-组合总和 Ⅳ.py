"""
middle 2021-08-18 dp完全背包
“考虑排列顺序的完全背包问题”，外层循环为 target ，内层循环为选择池 nums。
dp[i] 表示和为 i 的 num 组合有 dp[i] 种。
https://leetcode-cn.com/problems/coin-change/solution/yi-tao-kuang-jia-jie-jue-bei-bao-wen-ti-h0y40/
"""
class Solution:
    def combinationSum4(self, nums, target):
        dp = [0] * (target+1) # 和为 i 的 num 组合有 dp[i] 种
        dp[0] = 1 # 当不选取任何元素时，元素之和才为 0，因此只有 1 种方案
        for i in range(1, target + 1): # 外层循环target
            for num in nums: # 内层循环arrs
                if num <= i: # 物品体积不能大于背包容量
                    dp[i] += dp[i - num] # 求方案数套路
        return dp[target]


if __name__ == '__main__':
    nums = [1,2,3]
    target = 4
    print(Solution().combinationSum4(nums, target))