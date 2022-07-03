"""
middle 2021-10-26 【单调递减栈】
# 从后往前维护一个单调递减栈[4 2]
# 若出现了栈顶元素比当前元素小的情况
# 说明找到了一个中间元素，大于它后面的元素 [1 4 2] 1<4
# 与此同时由于单调栈的特性我们维护的这个“后面的元素”会尽可能大，只要存在一个前面的元素比它小即可
# ai<ak<aj
# i<j<k
https://leetcode-cn.com/problems/132-pattern/solution/xiang-xin-ke-xue-xi-lie-xiang-jie-wei-he-95gt/
"""
# 2021-12-16
class Solution:
    def find132pattern(self, nums):
        if not nums: return False
        stk = []
        aj = float('-inf')
        for i in range(len(nums)-1,-1,-1):
            # 这里说明找到了ai，遍历到1的时候，1<4，找到了
            # 同时逆向的单调递减栈保证了，cur(ak)一定大于aj
            if nums[i]<aj: return True
            # 栈里维护最大的元素
            while stk and nums[i]>nums[stk[-1]]: # 如果不满足单调递减的性质，即情况4 2
                # 那么aj即2出栈，这时候已经有4了
                aj = nums[stk[-1]] # aj是被出栈的，次于cur的值
                # print("s3:",ak)
                stk.pop()
            stk.append(i) # 4 入栈
            # print("stk:",stk)
        return False

"""
还可以直接存数值
class Solution:
    def find132pattern(self, nums):
        stack = []
        _MIN = float('-inf')
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < _MIN:
                return True
            while stack and nums[i] > stack[-1]:
                _MIN = stack.pop()
            stack.append(nums[i])
        return False
"""

if __name__ == '__main__':
    # nums = [1, 2, 3, 4] #f
    nums = [3, 1, 4, 2]  # t
    res = Solution()
    print(res.find132pattern(nums))