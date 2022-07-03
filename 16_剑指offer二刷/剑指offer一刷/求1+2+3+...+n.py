# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.res = 0
    def Sum_Solution(self, n):
        # write code here
        self.res += n
        n>0 and self.Sum_Solution(n-1)
        return self.res


if __name__ == '__main__':
    n = 2
    print(Solution().Sum_Solution(n))