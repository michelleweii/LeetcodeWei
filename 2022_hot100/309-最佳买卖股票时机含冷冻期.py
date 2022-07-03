"""
middle 2022-01-27 2维dp
# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。【卖出之后有限制】
状态定义：dp[i][j] 表示 [0, i] 区间内，在下标为 i 这一天状态为 j 时，我们手上拥有的金钱数。
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solution/mai-mai-gu-piao-wen-ti-by-chen-wei-f-xvs1/
"""
# 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
# 0 持有现金
# 1 持有股票，只有从第一天开始交易以后才有此状态，没有交易前i<0时，该状态都是不存在-int('inf')
class Solution:
    def maxProfit(self, prices):
        if not prices: return 0
        if len(prices) == 1: return 0
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n)]
        # 初始化
        dp[0][0] = 0 # 第0天，持有现金为0
        dp[0][1] = -prices[0] # 第0天，持有股票-prices[0]
        dp[1][0] = max(0, prices[1]-prices[0])# 第1天，持有现金(需要第0天买入，第1天卖出)
        dp[1][1] = max(-prices[0], -prices[1])# 第1天，持有股票(第0天买股票，第1天可以不操作)
        # 状态转移
        for i in range(2, n):
            # 股票：买股票，可以什么都不做+可以从持有现金状态转为持有股票状态
            # 卖出 ---- 冷冻期 ----  买入
            dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])
            # 现金：卖股票，可以什么都不做+可以从股票状态转为现金状态
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
        return dp[-1][0]

if __name__ == '__main__':
    prices = [1,2,3,0,2]
    print(Solution().maxProfit(prices))