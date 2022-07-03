"""
easy 2022-06-22 大数问题——全排列

字符串全排列，解决大数问题

在数字很大的情况下，哪怕long类型也无法承载，那必须要用字符串保存。
对于本题其实就是对数字0~9的全排列，从1位数0~9的全排列到n位数0~9的全排列，其中要注意的是数字开头不应该有0。

链接：https://leetcode.cn/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/solution/jian-zhi-offer-17-da-yin-cong-1dao-zui-d-ngm4/

时间复杂度：O(10^n)，从 1 到 10^n-1的数肯定都遍历了一遍
空间复杂度：O(n)，空间复杂度度主要在递归栈以及num数组这里，递归的最大深度和数组的最大长度都为n；算返回值的话为O(10^n)
"""
class Solution:
    def printNumbers(self, n: int):#-> List[int]:
        # 全排列回溯
        def dfs(index, digit, num):
            # index 目前到几位数了， if index == digit, 说明已经生成了题目要求
            # 用digit表示要生成的数字的位数
            # num当前第几位数，所含的all第几位数
            if index == digit:  # index=1
                res.append(int(''.join(num)))
                return
            for i in range(10):
                num.append(str(i))
                dfs(index + 1, digit, num)
                num.pop()  # 回溯

        ## 开始
        res = []
        for digit in range(1, n + 1):  # 是几位数，1,2,3
            for first in range(1, 10):  # 1.为了避免数字开头出现0，先把首位first固定，first取值范围为1~9
                num = [str(first)]  # num=1~9
                dfs(1, digit, num)  #

        return res

if __name__ == '__main__':
    n=2
    print(Solution().printNumbers(n))