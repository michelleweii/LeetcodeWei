"""
middle 2022-01-27 2维dp
dp[i][j] 表示 [0, i] 区间内，在下标为 i 这一天状态为 j 时，我们手上拥有的金钱数。
每次交易要支付手续费 我们定义在卖出的时候扣手续费
LC122扩展
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solution/mai-mai-gu-piao-wen-ti-by-chen-wei-f-xvs1/
"""
# 0 持有现金
# 1 持有股票，只有从第一天开始交易以后才有此状态，没有交易前i<0时，该状态都是不存在-int('inf')
class Solution:
    def maxProfit(self, prices, fee):
        if not prices: return 0
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n)]

        # 初始化
        dp[0][0] = 0 # 持有现金
        dp[0][1] = -prices[0] # 持有股票

        for i in range(1, n):
            # 从持有现金的状态，转为持有股票的状态
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
            # 从持有股票的状态，转为持有现金的状态
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]-fee) # 定义在卖出的时候扣手续费
        return dp[-1][0]

if __name__ == '__main__':
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    print(Solution().maxProfit(prices,fee))