# -*- coding:utf-8 -*-

# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
class Solution:
    def NumberOf1(self, n):
        res = 0
        for i in range(32):
            res+=(n&1)
            n = n>>1
        return res


if __name__ == '__main__':
    n=-10
    print(Solution().NumberOf1(n))