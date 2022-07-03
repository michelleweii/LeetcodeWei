"""
middle 2021-08-18 完全背包
是否可以用 coins 中的数组合和成 amount，完全背包问题，并且为“不考虑排列顺序的完全背包问题”，外层循环为选择池 coins，内层循环为 amount。
dp[i] 表示和为 i 的 coin 组合有 dp[i] 种。
https://leetcode-cn.com/problems/coin-change/solution/yi-tao-kuang-jia-jie-jue-bei-bao-wen-ti-h0y40/
"""
class Solution:
    def change(self, amount, coins):
        # dp[i] 表示和为 i 的 coin 组合有 dp[i] 种。
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1 # 只有当不选取任何元素时，元素之和才为 0，因此只有 1 种方案
        for coin in coins: # 外层arrs
            for i in range(amount+1): # 内层target
                # 物品体积不能大于背包容量
                if i>=coin:
                    dp[i] = dp[i]+dp[i-coin]
        return dp[amount]

if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]
    print(Solution().change(amount,coins))