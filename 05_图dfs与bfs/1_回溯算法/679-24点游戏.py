"""
hard 2022-05-08 回溯
https://leetcode-cn.com/problems/24-game/solution/python-zui-jia-da-an-by-lu-ma-b-bdjv/
## 抖音：抖音算法一面，判断 任意给四个数字和一个target，是否存在这样一个等式。
### 进阶（微软）:要求将符合的表达式输出。https://leetcode-cn.com/problems/24-game/solution/jin-jie-fan-hui-jie-guo-bing-qie-da-yin-xcl05/
"""
import math
class Solution:
    def judgePoint24(self, cards): #List[int]) -> bool:
        # 递归出口
        if len(cards)==1:# return cards[0]==24 #
            return math.isclose(cards[0],24) # 由于小数除法有误差 所以最后判断和24的差值是否充分小
        for _ in range(len(cards)):
            a = cards.pop(0) # 摸一张
            for _ in range(len(cards)): # 这里不能使用固定的n=len(cards), 因为cards的数值会随着pop变动
                b = cards.pop(0) # 再摸一张
                # 计算a与b的运算结果
                for value in [a+b,a-b,a*b,b and a/b]:
                    cards.append(value)
                    if self.judgePoint24(cards):return True
                    cards.pop() # 先回溯a+b，再回溯a-b。。。
                cards.append(b) # 回溯b
            cards.append(a) # 回溯a
        return False

if __name__ == '__main__':
    cards = [4, 1, 8, 7]
    print(Solution().judgePoint24(cards))
    # print("sda:{}".format('daksnofwof'))