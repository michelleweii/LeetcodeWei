"""
middle 2022-01-17 回溯
https://www.programmercarl.com/0491.%E9%80%92%E5%A2%9E%E5%AD%90%E5%BA%8F%E5%88%97.html#%E6%80%9D%E8%B7%AF
【重点】题目不能排序。本题求自增子序列，是不能对原数组经行排序的，排完序的数组都是自增子序列了。
【重点】unordered_set<int> uset; 是记录本层元素是否重复使用，新的一层uset都会重新定义（清空），所以要知道uset只负责本层！
"""
class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def findSubsequences(self, nums): #List[int]) -> List[List[int]]:
        # nums.sort() # 本题求自增子序列，是不能对原数组经行排序的，排完序的数组都是自增子序列了。
        # used = [0]*201
        self.backtrace(nums, 0)
        # self.backtrace2(nums, 0, used) # 失败，因为nums没有sort，
        # if i>0 and nums[i]==nums[i-1] and used[i-1]==0:
        return self.res

    def backtrace(self, nums, start_index):
        # 收集结果，同78.子集，仍要置于终止条件之前
        if len(self.path) > 1: # 题目要求至少2个节点
            # 本题要求所有的节点
            self.res.append(self.path[:])
            # 注意这里不要加return，要取树上的all节点

        if start_index>=len(nums):return # 可有可无，下方for训练到头自然会结束

        # 单层递归逻辑
        # 【深度遍历中每一层都会有一个全新的usage_list用于记录本层元素是否重复使用】
        # 【Attention】
        used = [False]*201 #  # 使用列表去重，题中取值范围[-100, 100]
        for i in range(start_index, len(nums)): # 树层遍历
            # 剪枝
            # 若当前元素值小于前一个时（非递增）或者曾用过，跳入下一循环
            if (self.path and nums[i] < self.path[-1]) or used[nums[i]] == True:
                continue
            # 回溯
            used[nums[i]] = True
            self.path.append(nums[i])
            self.backtrace(nums, i+1)
            # used[i] = 0
            self.path.pop()

            """
            if i>start_index and nums[i]==nums[i-1]:continue
            ERROR
            [4,4,3,2,1], [[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,4],[1,2,4],[1,2,4,4],[1,3],[1,3,4],[1,3,4,4],[1,4],[1,4,4],[2,3],[2,3,4],[2,3,4,4],[2,4],[2,4,4],[3,4],[3,4,4],[4,4]]
            ANSWER [[4,4]]
            """

    # def backtrace2(self, nums, start_index, used):
    #     if len(self.path)>=2:
    #         self.res.append(self.path[:])
    #
    #     if start_index>=len(nums):return
    #
    #     for i in range(start_index, len(nums)):
    #         self.path.append(nums[i])
    #
    #         # 剪枝
    #         if self.path and nums[i]<self.path[-1]:
    #             continue
    #
    #         if used[nums[i]]==1:continue # 同层
    #
    #         used[nums[i]] = 1
    #         self.path.append(nums[i])
    #         self.backtrace2(nums,i+1,used)
    #         used[nums[i]] = 0
    #         self.path.pop()


if __name__ == '__main__':
    nums = [4, 6, 7, 7]
    # [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
    # nums = [4,4,3,2,1]

    print(Solution().findSubsequences(nums))