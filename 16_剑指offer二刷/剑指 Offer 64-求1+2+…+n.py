"""
middle 逻辑and or
2021-07-19
"""

class Solution:
    def __init__(self):
        self.res = 0
    def sumNums(self, n):
        n>1 and self.sumNums(n-1) # 注意这里是个语句，不是个条件
        self.res += n
        return self.res

if __name__ == '__main__':
    n = 3
    print(Solution().sumNums(n))