"""
easy 位运算
2021-07-13
"""

class Solution:
    def hammingWeight(self, n):
        res = 0
        for i in range(32):
            res += n&1
            n = n>>1
        return res


if __name__ == '__main__':
    n = 128
    print(Solution().hammingWeight(n))