"""
middle 模拟题
2021-07-20
越界判断的思路很好
https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/
"""
# ord('a') 97
# ord('c') 99
# 字符转数字： “此数字的 ASCII 码” 与 “0 的 ASCII 码” 相减即可；
class Solution:
    def strToInt(self, strs: str) -> int:
        res, sign = 0, 1
        strs = strs.strip()
        if not strs:return 0
        for i in range(len(strs)):
            ch = strs[i]
            if i == 0 and (ch == '-' or ch == '+'):
                if ch == '-': sign = -1
                if ch == '+': sign = 1
                continue  # 应对-123,是+-号之后就不用判断是否数字了
            if not ch.isdigit(): break  # 如果不是数字
            res = 10 * res + ord(ch) - ord('0')
        # 如果下越界 就返回-2**31 如果上越界返回2**31-1
        return max(-2 ** 31, -1 * res) if sign == -1 else min(2 ** 31 - 1, res)

if __name__ == '__main__':
    s = "   -42"
    print(Solution().strToInt(s))