"""
middle 2022-01-06 回溯
https://programmercarl.com/0216.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CIII.html#%E5%9B%9E%E6%BA%AF%E4%B8%89%E9%83%A8%E6%9B%B2
和为 n 的 k 个数的组合, 组合中只允许含有 1-9 的正整数，每种组合中不存在重复的数字。
题目：本题就是在[1,2,3,4,5,6,7,8,9]这个集合中找到和为n的k个数的组合（不重复）。
"""
class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def combinationSum3(self, k, n):
        if not n:return self.res
        nums = [i for i in range(1,10)] # 这里面没有重复元素，所以必然『每种组合中不存在重复的数字』
        self.dfs(nums,k,n,0,0)
        return self.res

    def dfs(self,nums,k,n,start_index,sums):
        # 剪枝
        if sums>n: return
        # 定义出口
        if len(self.path)==k and sums==n:
            self.res.append(self.path[:])
            return

        for i in range(start_index, len(nums)):
            # 剪枝
            if nums[i]>n or k<0:
                return

            sums += nums[i]
            self.path.append(nums[i])
            self.dfs(nums,k,n,i+1,sums) # 向下一层开始dfs
            sums -= nums[i]
            self.path.pop() # 回溯

if __name__ == '__main__':
    k = 3
    # n = 9
    n = 7
    print(Solution().combinationSum3(k,n))