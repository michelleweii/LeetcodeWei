"""
hard 2022-01-27 3维dp
题目要求只能完成2笔交易，之前都是无限次操作。
状态定义：dp[i][k][j] 表示到下标为 i 的这一天，最多进行k次交易，持股状态为j时，拥有的最大现金数。
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/solution/tong-su-yi-dong-de-dong-tai-gui-hua-jie-fa-by-marc/
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/solution/shu-ju-jie-gou-he-suan-fa-dong-tai-gui-h-qmhw/
"""
# 0 持有现金
# 1 持有股票，只有从第一天开始交易以后才有此状态，没有交易前i<0时，该状态都是不存在-int('inf')
class Solution:
    def maxProfit(self, prices):
        if not prices:return 0
        n = len(prices)
        if n==1:return 0
        # 结束时的最高利润=[第i天数][卖出次数][是否持有股票]
        # [i,j]第i天，j持股状态。3是交易次数（0、1、2笔）
        # int[][][] dp = new int[prices.length][3][2];
        dp = [[[0, 0] for _ in range(3)] for _ in range(n)]
        # # 最后一天，最多进行k次交易（存在0\1\2笔交易数状态），持股（要买股票）
        # 【在没有进行股票交易时不允许持有股票】
        for k in range(3): # 不存在的一天，还持股，不可能。
            dp[-1][k][1] = -float("inf")
        print(dp)
        # 一次都不交易，持有股票也是不存在的状态
        for i in range(n):
            dp[i][0][1] = -float("inf")

        for i in range(n):
            for k in range(1,3):# 最多只能买卖2次
                # 最多可以完成 两笔 交易，定义最多可以买2次股票
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i]) # 卖股票变成现金状态
                # [1]，从现金状态买入股票，转为持有股票状态
                # 买入一次，减去一次交易机会
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i]) # 买股票变成持股状态，买股票消耗一次机会
        return dp[-1][2][0]


if __name__ == '__main__':
    # prices = [3,3,5,0,0,3,1,4]
    # prices = [1, 2, 3, 4, 5] # 4
    prices = [7,6,4,3,1] # 0
    print(Solution().maxProfit(prices))