"""
easy 2022-01-04 同向双指针
https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/solution/tong-xiang-shuang-zhi-zhen-bian-xing-by-hr5zk/
双指针挺绝的，用栈算是easy
"""
class Solution:
    def removeDuplicates(self, s):
        ss = list(s)
        left, right = -1, 0
        n = len(ss)
        while right < n:
            if left == -1 or ss[left]!=ss[right]:
                left += 1
                ss[left] = ss[right]
                right += 1
            else:
                right += 1
                left -= 1
        return "".join(ss[:left+1])
#     """ 栈
#     stk = list()
#     for ch in s:
#         if stk and stk[-1] == ch:
#             stk.pop()
#         else:
#             stk.append(ch)
#     return "".join(stk)
# 链接：https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/solution/tu-jie-guan-fang-tui-jian-ti-jie-shan-ch-x8iz/
#     """

if __name__ == '__main__':
    s = "abbaca"
    ans = Solution()
    print(ans.removeDuplicates(s)) # "ca"
    # 在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。
    # 之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。
