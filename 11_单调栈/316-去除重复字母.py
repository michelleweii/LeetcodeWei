"""
middle 2021-12-16 单调递增栈
题目：去重+字典序最小——找最小——>单调递增栈
先做402再做316
https://leetcode-cn.com/problems/remove-duplicate-letters/solution/yi-zhao-chi-bian-li-kou-si-dao-ti-ma-ma-zai-ye-b-4/
思路：
1、key 为字符c，value为其出现的剩余次数
2、从左往右遍历字符串，每次遍历到一个字符，其剩余出现次数-1
3、对于每一个字符，如果其对应的剩余出现次数大于 1，我们可以选择丢弃（也可以选择不丢弃），否则不可以丢弃。【去重要有重复才能去，没有重复直接保留】
4、是否丢弃的标准和lc402类似。如果栈中相邻的元素字典序更大，那么我们选择丢弃相邻的栈中的元素。
"""
# print('a'<'b') # True
import collections
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stk = []
        remain_char = collections.Counter(s)
        visited = set() # 空间换时间
        # print(remain_char) # Counter({'c': 4, 'b': 2, 'a': 1, 'd': 1})
        for ch in s:
            # 根据题意去重，因为是单增，所以小的字符一定要在靠前的位置
            # if ch not in stk: # 判断当前字符是否在栈上存在需要 O(N) 的时间
            if ch not in visited: #  hashset,  O(1) 的时间
                # 维护单调递增栈
                # 根据题意增加判断。重复的元素才删除，如果只剩一个，就不删了
                while stk and ch<stk[-1] and remain_char[stk[-1]]>0:
                    # 具体操作，单调栈根据题意修改
                    t = stk.pop()
                    visited.remove(t)
                stk.append(ch)
                visited.add(ch)

            remain_char[ch] -= 1

        return ''.join(stk)

if __name__ == '__main__':
    # s = "bcabc" # "abc"
    s = "cbacdcbc" # "acdb"
    print(Solution().removeDuplicateLetters(s))