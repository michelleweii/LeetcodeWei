"""
股票问题通解：https://leetcode.cn/circle/article/qiAgHn/
easy 2022-01-27 一维dp
https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/solution/mian-shi-ti-63-gu-piao-de-zui-da-li-run-dong-tai-2/
状态定义：dp[i]代表以 prices[i]为结尾的子数组的最大利润（以下简称为 前 i 日的最大利润 ）
由于题目限定 “买卖该股票一次” ，因此前 i 日最大利润 dp[i] 等于前i−1日最大利润dp[i−1]和第i日卖出的最大利润中的最大值。
转移方程：前i日最大利润=max(前(i−1)日最大利润,第i日价格−前i日最低价格)
dp[i]=max(dp[i−1],prices[i]−min(prices[0:i]))
"""
class Solution(object):
    # 只要考虑当天买和之前买哪个收益更高，当天卖和之前卖哪个收益更高
    # dp[i]以 prices[i]为结尾的子数组的最大利润（以下简称为 前 i 日的最大利润 ）
    # 扩展可以交易两次（买卖算一次交易）求最大值
    def maxProfit_dp(self, prices):
        if not prices: return 0
        dp = [0 for _ in range(len(prices))]
        cost = prices[0]
        for i in range(1, len(prices)):
            cost = min(cost, prices[i])
            dp[i] = max(dp[i-1], prices[i]-min(cost, prices[i]))
        return max(dp)

    def maxProfit(self, prices):
        # 在价格最低的时候买入，差价最大的时候卖出
        if len(prices) < 2: return 0
        cost = prices[0] # 每日更新最低价格
        profit = 0 # 首日利润为0
        for price in prices:
            cost = min(cost, price) # 找到最低那天的价格
            profit = max(profit, price-cost)
        return profit


if __name__ == '__main__':
    prices = [7,6,4,3,1]
    print(Solution().maxProfit(prices))