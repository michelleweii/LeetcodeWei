"""
middle 2021-08-24 回溯法-分割问题-有startindex,
startIndex，因为切割过的地方，不能重复切割，和组合问题也是保持一致的。
"""
class Solution(object):

    def __init__(self): # 类变量
        self.res = [] # 总的结果
        self.path = [] # 以每个点开始的，当前路径结果(当前的方案)

    def partition(self, s):
        if not s:return self.res
        self.dfs(s,0) # 当前字符串，从下标0开始，样本
        return self.res

    def dfs(self, s, start_index):
        # 定义出口
        # 切割线切到了字符串最后面，说明找到了一种切割方法
        if start_index==len(s):
            self.res.append(self.path[:])

        for i in range(start_index, len(s)):
            # 是否有剪枝呢?
            p = s[start_index:i+1] # 分割问题
            if p!=p[::-1]:continue
            self.path.append(p)
            self.dfs(s,i+1)
            self.path.pop()


if __name__ == '__main__':
    # s = "aab"
    # s = "aba"
    s = 'a'
    myResult = Solution()
    print(myResult.partition(s))
    # print(myResult.check(s))