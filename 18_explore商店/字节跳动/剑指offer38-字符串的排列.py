

# 不能有重复元素
class Solution:
    def permutation(self, s): #str) -> List[str]:
        if not s:return []
        self.res, self.path = [], []
        s = [c for c in s]
        s.sort()
        used = [0]*len(s)
        self.backtrace(s,used)
        return self.res

    def backtrace(self,s,used):
        if len(self.path)==len(s):
            self.res.append(''.join(self.path))

        for i in range(len(s)):
            # s[i-1]==0 树层
            if i>0 and s[i]==s[i-1] and used[i-1]==0:continue

            # 树枝上，例如1,2,3 选过1之后，在2,3这轮，不能选1了
            if used[i]==1: continue

            # 正常回溯流程
            self.path.append(s[i])
            used[i]=1
            self.backtrace(s,used)
            self.path.pop()
            used[i]=0

if __name__ == '__main__':
    s = "aab"
    # 输出：["abc", "acb", "bac", "bca", "cab", "cba"]
    print(Solution().permutation(s))