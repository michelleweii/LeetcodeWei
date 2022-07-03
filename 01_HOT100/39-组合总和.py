"""
middle 2022-01-13 dfs回溯
题目画重点：1）一个无重复元素的数组；2）candidates 中的数字可以无限制重复被选取
https://programmercarl.com/0039.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8C.html#%E5%9B%9E%E6%BA%AF%E4%B8%89%E9%83%A8%E6%9B%B2
"""
# 给定一个(无重复元素)的数组 candidates 和一个目标数 target，
# 找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的数字可以无限制重复被选取。
class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def combinationSum(self, candidates, target):
        # 首先要排序，必不可少，记得归纳总结这里，什么时候要排序？？数组有重复元素则需要sort，数组无重复元素则不要sort
        # 这里开启的原因：为了剪枝需要提前进行排序
        candidates.sort() # 不需要
        self.dfs(candidates, target, 0, 0)
        return self.res

    def dfs(self,candidates, target, sums, start_index):
        if sums==target:
            self.res.append(self.path[:])
            return

        if sums > target:
            return

        for i in range(start_index, len(candidates)):
            # 剪枝, 为了剪枝需要提前进行排序
            if sums+candidates[i]>target:
                return
            # 回溯
            self.path.append(candidates[i])
            sums+=candidates[i]
            self.dfs(candidates,target,sums,i) # 不用i+1了，表示可以重复读取当前的数
            self.path.pop()
            sums-=candidates[i]


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    print(Solution().combinationSum(candidates,target))
    # 输出: [[7],[2,2,3]]