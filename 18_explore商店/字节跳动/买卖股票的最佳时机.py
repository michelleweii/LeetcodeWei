
# 2022-03-01
# 选择价格最低的日子买入，价格最高的日子卖出
class Solution:
    def maxProfit(self, prices):
        if not prices:return 0
        cost = prices[0]
        income = 0
        for i in range(1,len(prices)):
            income = max(income, prices[i]-cost)
            cost = min(cost, prices[i])
        return 0

if __name__ == '__main__':
    prices = [7,6,4,3,1]
    print(Solution().maxProfit(prices))