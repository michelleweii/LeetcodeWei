"""
middle 2022-01-14 回溯法-子集问题（有重复元素）
（used的使用看图）https://www.programmercarl.com/0090.%E5%AD%90%E9%9B%86II.html#_90-%E5%AD%90%E9%9B%86ii
子集问题，树枝上的所有节点都要。
*） nums有重复元素&解集不能包含重复元素。
"""
class Solution(object):
    def __init__(self):
        self.res = []
        self.path = []

    def subsetsWithDup(self, nums):
        if not nums:return self.res
        nums.sort()
        # 方法一：
        # self.dfs(nums,0)
        # 方法二：使用used标记访问
        used = [0]*len(nums)
        self.dfs_used(nums,0,used)
        return self.res

    def dfs_used(self,nums,start_index,used):
        self.res.append(self.path[:])
        # 定义出口
        if start_index>=len(nums):
            return
        # for循环控制树层
        for i in range(start_index, len(nums)):
            if i>0 and nums[i]==nums[i-1] and used[i-1]==0:
                continue
            self.path.append(nums[i])
            used[i] = 1
            self.dfs_used(nums,i+1,used) # start_index下一位开始
            self.path.pop()
            used[i] = 0

    # 方法一
    def dfs(self,nums,start_index):
        self.res.append(self.path[:])
        # 定义出口
        if start_index>=len(nums):
            return

        for i in range(start_index, len(nums)):
            # i是控制树层，取过的元素不再重复取，避免重复解
            if i>start_index and nums[i]==nums[i-1]:
                continue
            self.path.append(nums[i])
            self.dfs(nums,i+1) # i+1,取过的元素不能重复取
            self.path.pop()

if __name__ == '__main__':
    nums = [1,2,2]
    # nums = [0]
    print(Solution().subsetsWithDup(nums))
