"""
easy 2021-12-22 贪心
情况一：账单是5，直接收下。
情况二：账单是10，消耗一个5，增加一个10
情况三：账单是20，优先消耗一个10和一个5，如果不够，再消耗三个5;
-> 局部最优：遇到账单20，优先消耗美元10，完成本次找零。全局最优：完成全部账单的找零。
"""
class Solution:
    def lemonadeChange(self, bills) -> bool:
        five, ten, twenty = 0, 0, 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five < 1: return False
                five -= 1
                ten += 1
            else: #20
                if ten>0 and five>0:
                    ten-=1
                    five-=1
                    twenty+=1
                elif five>=3:
                    five-=3
                    twenty+=1
                else:
                    return False
        return True



if __name__ == '__main__':
    bills = [5, 5, 5, 10, 20]
    print(Solution().lemonadeChange(bills))