"""
middle 2022-01-14 回溯法-子集问题（无重复元素）
子集问题，树枝上的所有节点都要（遍历整棵树）。解集不能包含重复的子集start_index+1。
输入: nums = [1,2,3] 输出: [ [3], [1], [2], [1,2,3], [1,3], [2,3], [1,2], [] ]
"""
class Solution(object):
    def __init__(self):
        self.res = []
        self.path = []

    def subsets(self, nums):
        if not nums:return self.res
        self.dfs(nums,0)
        return self.res

    def dfs(self,nums,start_index):
        self.res.append(self.path[:]) # 与出口的前后顺序不能交换，否则包含最后一位的结果不会添加至res
        # 定义出口
        if start_index>=len(nums):
            return
        # 树层for循环
        for i in range(start_index, len(nums)):
            self.path.append(nums[i])
            # 树枝递归
            self.dfs(nums,i+1) # i+1 取过的位置，的下一位开始(元素不重复取)
            self.path.pop()

if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().subsets(nums))
    # [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
