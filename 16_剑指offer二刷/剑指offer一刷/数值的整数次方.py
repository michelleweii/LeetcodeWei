# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        flag = 0
        res = 1
        if exponent<0:
            flag=1
        for i in range(abs(exponent)):
            res *= base
        if flag:
            return 1/res
        else:
            return res

if __name__ == '__main__':
    base = 3
    e = -2
    print(Solution().Power(base,e))