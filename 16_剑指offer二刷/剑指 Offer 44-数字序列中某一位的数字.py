"""
middle 找规律
2021-07-20
不用再做了，放弃了
https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/solution/mian-shi-ti-44-shu-zi-xu-lie-zhong-mou-yi-wei-de-6/
"""
class Solution:
    def findNthDigit(self, n: int) -> int:
        digit, start, count = 1, 1, 9 # 数字，第几位数，数位数量
        while n>count:
            n -= count
            start *= 10  # 1, 10, 100, ...
            digit += 1  # 1,  2,  3, ...
            count = 9 * start * digit  # 9, 180, 2700, ...
        num = start + (n - 1) // digit  # 2.
        return int(str(num)[(n - 1) % digit])  # 3.

if __name__ == '__main__':
    n = 11
    print(Solution().findNthDigit(n))