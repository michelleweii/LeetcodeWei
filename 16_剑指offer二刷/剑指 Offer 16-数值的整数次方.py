"""
middle 快速幂
https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/solution/mian-shi-ti-16-shu-zhi-de-zheng-shu-ci-fang-kuai-s/
"""
class Solution:
    # 超出时间限制
    def myPow(self, x: float, n: int) -> float:
        if n==0:return 1
        sign = 0
        if n<0:
            sign = 1
            n = -n
        res = 1
        while n:
            if n&1: # 相当于对n%2
                res *= x
            x *= x
            n = n>>1 # 相当于除以2
        if sign:
            return 1/res
        return res

    # 更为优美的 快速幂
    def myPow_better(self, x: float, n: int) -> float:
        if x == 0: return 0
        res = 1
        if n < 0: x, n = 1 / x, -n
        while n:
            if n & 1: res *= x
            x *= x
            n >>= 1
        return res

    # 一般乘法
    def myPow1(self, x: float, n: int) -> float:
        res = 1
        for i in range(1, abs(n)+1):
            res *= x
        if n < 0:
            res = 1 / res
        return res


if __name__ == '__main__':
    # x = 2.00000
    # n = 10
    x = 2
    n = -2
    print(Solution().myPow(x, n))