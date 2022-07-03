"""
middle 2021-12-15 栈【字节面试题】
要实现分配律的规则：如3[a2[c]b] 使用一次分配律-> 3[accb] 再使用一次分配律->accbaccbaccb
https://leetcode-cn.com/problems/decode-string/solution/decode-string-fu-zhu-zhan-fa-di-gui-fa-by-jyd/
https://leetcode-cn.com/problems/decode-string/solution/zhan-de-ji-yi-nei-ceng-de-jie-ma-liao-bie-wang-lia/
还要重做呀~！
"""
class Solution:
    def decodeString(self, s: str) -> str:
        # 【核心思想】
        # 碰到[,"数字和当前字符串"入栈，
        # 碰到],"数字和字符串"出栈
        # 栈 index=0: [之前的倍数
        # 栈 index=1: [之前的临时结果
        stack = []
        res = ""
        multi = 0 # 倍数
        for c in s:
            if c=='[':
                stack.append([multi, res]) # 此 [ 前的临时结果 res 至栈
                res, multi = "", 0
            elif c==']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi*res
            # last_res是上个 [ 到当前 [ 的字符串，例如 "3[a2[c]]" 中的 a；
            # cur_multi是当前 [ 到 ] 内字符串的重复倍数，例如 "3[a2[c]]" 中的 2
            elif '0' <= c <= '9': # e.g.23
                multi = multi*10+int(c)
            else:
                res += c # res是[前的临时结果，进行字符拼接
        return res

if __name__ == '__main__':
    s = "3[a2[c]]" # "acc acc acc"
    print(Solution().decodeString(s))