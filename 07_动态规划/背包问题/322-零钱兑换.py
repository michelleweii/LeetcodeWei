"""
middle 2022-01-25 dp完全背包
完全背包问题——填满容量为amount的背包最少需要多少硬币
[数组中的元素可重复使用并且不考虑元素之间顺序]
"""
# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的
# 最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
class Solution(object):
    def coinChange2022(self, coins, amount):
        max_int = 2 << 31
        dp = [max_int]*(amount+1) # 构成金额i的最少硬币数
        dp[0] = 0  # 构成金额0，需要0个硬币数
        for coin in coins: # 外层遍历arrs
            for i in range(amount+1): # 内层遍历target
                # 物品体积不能大于背包容量
                if coin<=i:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return -1 if dp[amount]==max_int else dp[amount]
# 设dp[i]为构成金额i的最优解,即凑成总金额所需的最少的硬币个数
# 那么dp[1]=1,dp[2]=1,dp[5]=1,因为coins中有此金额，直接拿来用即可
# dp[i]=min(dp[i-1],dp[i-2],dp[i-5])+1
if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    print(Solution().coinChange2022(coins,amount))



