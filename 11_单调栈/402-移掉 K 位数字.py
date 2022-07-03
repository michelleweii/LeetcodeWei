"""
middle 2021-12-16 单调递增栈
题目：移除这个数中的 k 位数字，使得剩下的数字最小。
https://leetcode-cn.com/problems/remove-duplicate-letters/solution/yi-zhao-chi-bian-li-kou-si-dao-ti-ma-ma-zai-ye-b-4/
# ------------ 前置知识 -------------
# 对于两个数 123a456 和 123b456，如果 a > b， 那么数字 123a456 大于 数字 123b456，
否则数字 123a456 小于等于数字 123b456。也就说，两个相同位数的数字大小关系取决于第一个不同的数的大小。
# ------------------------------------
【分析】：请你以字符串形式返回这个最小的数字。找小的数字——>单调递增栈
思路: 维护一个单调递增栈，模拟一遍
1、从左到右遍历
2、对于遍历到的元素，我们选择保留。
3、但是我们可以选择性丢弃前面相邻的元素。
"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []
        remain = len(num) - k
        # 提示： 如果题目改成求删除 k 个字符之后的最大数，我们只需要将 stack[-1] > digit 中的大于号改成小于号即可。
        for ch in num:
            while k and stk and int(ch)<int(stk[-1]):
                stk.pop()
                k -= 1
            stk.append(ch)

        # 裁掉左边的0，例如0200
        # 从原数字移除所有的数字，剩余为空就是 0
        return ''.join(stk[:remain]).lstrip('0') or '0'

if __name__ == '__main__':
    # num = "1432219"
    # k = 3 # "1219"
    # num = "10200"
    # k = 1 # "200"
    # num = "9"
    # k = 1
    num =  "1173"
    k = 2 # 11
    print(Solution().removeKdigits(num, k))