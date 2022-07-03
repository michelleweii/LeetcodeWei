"""
middle 2021-01-27 2维dp（字节）
dp[i][j] 表示到下标为 i 的这一天，持股状态为 j 时，我们手上拥有的最大现金数。
第一维 i 表示下标为 i 的那一天（ 具有前缀性质，即考虑了之前天数的交易 ）；
第二维 j 表示下标为 i 的那一天是持有股票，还是持有现金。这里 0 表示持有现金（cash），1 表示持有股票（stock）。
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/tan-xin-suan-fa-by-liweiwei1419-2/
"""
# 0 持有现金
# 1 持有股票，只有从第一天开始交易以后才有此状态，没有交易前i<0时，该状态都是不存在-int('inf')
class Solution:
    def maxProfit(self, prices):
        if not prices : return 0
        if len(prices)<2:return 0
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]
        dp[0][0] = 0 # 什么都不做，持有现金
        dp[0][1] = -prices[0] # 持有股票，第一天买入股票，持有现金数为负

        for i in range(1, n):
            # [0]现金状态，从持有股票的状态转来，再加上卖出股票的利润
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]) # 持有现金，股票要卖出
            # [1]持股状态，从现金状态转来，再减去买入股票的价格
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i]) # 持有股票，现金要减少
        return dp[-1][0]

    # 贪心做法，每天都可以买卖
    #     sum_num = 0
    #     for i in range(n - 1):
    #         if prices[i] < prices[i + 1]:
    #             sum_num += prices[i + 1] - prices[i]
    #     return sum_num

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))