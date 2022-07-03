"""
middle 2022-01-13 回溯|组合
# candidates 中(有重复元素！)的每个数字在每个组合中只能使用一次。
题目画重点：1）一个有重复元素的数组；2）candidates在每个组合中只能使用一次；
https://programmercarl.com/0040.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CII.html
"""
# 给定一个数组 candidates 和一个目标数 target ，
# 找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的每个数字在每个组合中只能使用一次。
# -----------------------------------------------
# 递归的时候将 idx 加 1（需判断是否超出candidates的范围），另外由于题目输入的candidates可能包含相同的元素，
# 所以我们需要对得到的答案进行去重处理。
class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def combinationSum2(self, candidates, target):
        candidates.sort() # 首先要排序
        self.dfs(candidates,target,0,0)
        return self.res

    # i+1表明一个数字只能使用一次
    def dfs(self,candidates,target,sums,start_index):
        # 判断出口
        if sums == target:
            self.res.append(self.path[:])
            return

        # 树层开始循环遍历
        for i in range(start_index,len(candidates)):
            # 剪枝
            if sums + candidates[i] > target:
                return
            # 要对同一树层使用过的元素进行跳过
            # 【核心】
            if i>start_index and candidates[i] == candidates[i-1]:continue

            sums+=candidates[i]
            self.path.append(candidates[i])
            # i+1表明一个数字只能使用一次，这样下次递归的循环就从i+1开始了
            self.dfs(candidates,target,sums,i+1) # 再向下一层
            sums-=candidates[i]
            self.path.pop()


if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    # candidates = [2,5,2,1,2]
    # target = 5
    print(Solution().combinationSum2(candidates, target))