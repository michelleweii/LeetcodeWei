

# 2022-03-01
# dp[i][j] 在第i天，手上拥有的最大现金数。
# j=0是持有现金，j=1是持有股票
# 可以买卖多次
class Solution:
    def maxProfit(self, prices):
        if not prices:return 0
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]
        # print(dp, len(dp), len(dp[0]))
        dp[0][0] = 0 # 持有现金，说明什么都没有买
        dp[0][1] = -prices[0] # 持有股票
        for i in range(1, n):
            # 状态转移：
            # dp[i][1] = # 只能从持有现金的状态转移过来，买股票，money--
            # dp[i][0] = # 只能从持有股票的的状态转移过来，卖股票，money++
            dp[i][1] = max(dp[i-1][0]-prices[i], dp[i-1][1])
            dp[i][0] = max(dp[i-1][1]+prices[i], dp[i-1][0])

        return dp[-1][0] # 最后一天，持有现金

if __name__ == '__main__':
    prices = [7,6,4,3,1]#[1, 2, 3, 4, 5]
    print(Solution().maxProfit(prices))