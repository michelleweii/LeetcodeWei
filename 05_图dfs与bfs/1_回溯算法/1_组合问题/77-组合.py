"""
middle 2022-01-06 回溯法|组合问题
https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html#%E5%9B%9E%E6%BA%AF%E6%B3%95%E4%B8%89%E9%83%A8%E6%9B%B2
# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
# 没有剪枝
# 与LC257树的回溯对比学习
"""
class Solution:
    def __init__(self):
        # 全局变量
        self.path = [] # 用来存放符合条件结果
        self.res = [] # 存放符合条件结果的集合

    def combine(self, n, k):
        if not k:return self.res
        self.dfs(n, k, 1) # 返回范围 [1, n] 中所有可能的 k 个数的组合
        return self.res

    def dfs(self, n, k, start_index):
        # dfs出口
        if len(self.path)==k:
            self.res.append(self.path[:])
            # return # return加不加都不影响结果，所以作用是什么？
        # 横向遍历
        # 每次从集合中选取元素，可选择的范围随着选择的进行而收缩，调整可选择的范围。
        # 图中可以发现n相当于树的宽度，k相当于树的深度。
        for i in range(start_index, n+1):
            # 剪枝?
            self.path.append(i) # 处理节点
            self.dfs(n,k,i+1) # 递归：控制树的纵向遍历，注意下一层搜索要从i+1开始
            self.path.pop() # 回溯，撤销处理的节点

if __name__ == '__main__':
    n = 4
    k = 2 # [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    print(Solution().combine(n,k))