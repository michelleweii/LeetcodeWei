"""
easy 2022-01-28 模拟题
https://leetcode-cn.com/problems/ugly-number/solution/gong-shui-san-xie-jian-dan-de-fen-qing-k-dlvg/
"""
# 判断一个数是否为丑数
# 如果 n 是正整数：我们对 n 执行 2 3 5 的整除操作即可，直到 n 被除干净，如果 n 最终为 1 说明是丑数，否则不是丑数。
class Solution(object):
    # 和求质数的思路一样
    # 每一个丑数必然是之前丑数与2，3或5的乘积得到的，这样下一个丑数就是用之前的丑数分别乘以2，3，5
    def isUgly(self, num):
        if num<=0: return False
        # 注意，2 3 5 先除哪一个都是可以的，因为乘法本身具有交换律。
        while (num % 2 == 0): num /= 2
        while (num % 3 == 0): num /= 3
        while (num % 5 == 0): num /= 5
        return num==1

if __name__ == '__main__':
    num = 14
    ans = Solution()
    print(ans.isUgly(num))