"""
middle 2021-01-07 回溯dfs
https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/solution/dai-ma-sui-xiang-lu-jian-zhi-offer-38-zi-gwt6/
本题是回溯算法经典题目，求全排列+去重，这道题目和 LC47.全排列II 几乎是一样的。

还有另外一种传参解法https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/solution/er-shua-quan-pai-lie-by-sharonjin-2nsx/
传参: 参数是path和idx下标, dfs(idx + 1, path + [ss[i]])
"""
class Solution:
    ######### 模板解法start ########
    def muban(self,s):
        self.res, self.path = [], []
        if not s:return self.res
        s = [x for x in s]
        s.sort()
        used = [0]*len(s)
        self.muban_dfs(s, used)
        return self.res

    def muban_dfs(self, s, used):
        if len(self.path)==len(s):
            self.res.append(''.join(self.path[:]))

        for i in range(len(s)):
            if i>0 and s[i-1]==s[i] and used[i-1]==0: continue # 树层上已经选过该字母充当首字母
            if used[i]==1: continue # 当前这个位置已经选过了
            used[i]=1
            self.path.append(s[i])
            self.muban_dfs(s, used)
            used[i]=0
            self.path.pop()
    ######### 模板解法end ########

    # # 如果参数是path和idx下标的话
    # def permutation(self, s: str) -> List[str]:
    #     n = len(s)
    #     ss = sorted(list(s))
    #
    #     ret = []
    #     visited = [False] * n
    #
    #     def dfs(idx, path):
    #         if idx == n:
    #             ret.append("".join(path))
    #             return
    #         for i in range(n):
    #             if visited[i] or (!visited[i - 1] and i > 0 and ss[i] == ss[i - 1]):
    #                 continue
    #             visited[i] = True
    #             dfs(idx + 1, path + [ss[i]])
    #             visited[i] = False
    #
    #     dfs(0, [])
    #     return ret

    ######## 错误解法start #######
    def permutation_error(self, s: str):
        self.path, self.res = [], []
        # 题目里可能会包含重复元素，需要sort
        # 字符串没有sort功能
        if not s:return self.res
        self.backbrace(s)
        return self.res

    # 回溯要求去重
    # 这种解法，会有重复元素
    def backbrace(self, s):
        if s=='':
            # print(self.path)
            self.res.append(''.join(self.path))

        for i in range(len(s)):
            self.path.append(s[i])

            self.backbrace(s[:i]+s[i+1:])
            self.path.pop()
    ######## 错误解法end #######


if __name__ == '__main__':
    # s = "abc" # ['acb', 'bca', 'cba', 'abc', 'bac', 'cab']
    s = "aab" # ['aab', 'aba', 'aab', 'aba', 'baa', 'baa'] error answer
    #                           ['aab', 'aba', 'baa'] # right answer
    # print(Solution().permutation(s))
    print(Solution().muban(s))
    # print(Solution().permutation2(s))
    # print(Solution().permutation3(s))