"""
middle 2022-01-17 回溯法-排列问题-无重复元素
https://www.programmercarl.com/0046.%E5%85%A8%E6%8E%92%E5%88%97.html#%E6%80%9D%E8%B7%AF
【重点】排列问题只要树的叶子节点，两个list可以交错插入，所以不需要从start_index开始；
(必须要有used，因为没有start_index了，所以不可以在用i>start_index来去重)
【重点】无重复元素不需要sort；
"""
class Solution(object):
    '''
    因为本题排列是有序的，这意味着同一层的元素可以重复使用，但同一树枝上不能重复使用
    所以处理排列问题每层都需要从头搜索，故不再使用start_index
    '''
    def __init__(self):
        self.res = []
        self.path = []

    def permute(self, nums):
        # 方法1
        # self.dfs(nums)
        # return self.res

        # 方法2，使用used作为标记
        used = [0]*len(nums)
        self.dfs_used(nums,used)
        return self.res

    def dfs_used(self,nums,used):
        # 定义出口
        if len(self.path)==len(nums):
            self.res.append(self.path[:])
            return

        # 树层遍历
        for i in range(len(nums)):
            if used[i] == 1:continue
            self.path.append(nums[i])
            used[i]=1 # 标记已访问过
            # 树枝递归
            self.dfs_used(nums,used)
            self.path.pop() # 回溯
            used[i]=0

    def dfs(self, nums):
        # 定义出口
        if len(self.path) == len(nums):
            self.res.append(self.path[:])  # 此时说明找到了一组
            return
        # 树层遍历
        for i in range(len(nums)):
            # 如果树层里
            if nums[i] in self.path:  # path里已经收录的元素，直接跳过
                continue
            self.path.append(nums[i])
            # 树枝递归
            self.dfs(nums)  # 递归
            self.path.pop()  # 回溯

if __name__ == '__main__':
    nums = [1, 2, 3]
    # nums = [1]
    print(Solution().permute(nums))





























