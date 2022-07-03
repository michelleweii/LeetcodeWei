"""
middle 2022-05-12 dfs
[很清晰的题解]
https://leetcode.cn/problems/longest-substring-with-at-least-k-repeating-characters/solution/jie-ben-ti-bang-zhu-da-jia-li-jie-di-gui-obla/
"""
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # 返回满足题意的最长子字符串长度
        if len(s)<k: return 0
        for c in set(s):
            if s.count(c)<k:
                # return max(self.longestSubstring(t, k) for t in s.split(c))
                # 下面这段都可以用上面一句代替
                tmp=[]
                for sub in s.split(c):
                    # 每个子串都调用func
                    tmp.append(self.longestSubstring(sub, k))
                return max(tmp)
        return len(s)


if __name__ == '__main__':
    s = "bbaaacbd" #"aaabb"
    # print(set(s)) # {'a', 'b'}
    k = 3
    print(Solution().longestSubstring(s,k))