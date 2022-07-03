"""
easy 2021-12- 位运算
题目：判断整数n是否是2的幂次方
方法一：log2n是否是整数
方法二：https://leetcode-cn.com/problems/power-of-two/solution/power-of-two-er-jin-zhi-ji-jian-by-jyd/
2进制理论，
"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0
        # print(math.log(n,2)) # 4.0 python返回的好像都是小数

if __name__ == '__main__':
    n = 16
    print(Solution().isPowerOfTwo(n))