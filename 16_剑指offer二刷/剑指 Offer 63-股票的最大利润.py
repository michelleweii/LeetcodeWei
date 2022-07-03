"""
middle 一维dp
2021-07-19
https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/solution/mian-shi-ti-63-gu-piao-de-zui-da-li-run-dong-tai-2/
"""
# dp[i] 为 第i天卖出的最大利润
# 扩展可以交易两次（买卖算一次交易）求最大值
class Solution:
    def maxProfit(self, prices):
        if not prices:return 0
        dp = [0 for _ in range(len(prices))]
        cost = prices[0]
        for i in range(1, len(prices)):
            cost = min(cost, prices[i])
            dp[i] = max(dp[i-1], prices[i]-min(cost, prices[i]))
        return max(dp)

if __name__ == '__main__':
    prices = [7,1,5,3,6,4] # 5
    # prices = [1,2] # 1
    print(Solution().maxProfit(prices))