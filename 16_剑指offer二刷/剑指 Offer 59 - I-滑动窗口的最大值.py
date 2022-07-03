"""
hard 单调栈
滑动窗口最大值——必会(单调栈里存的是下标)
2021-07-19
"""
class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums or not k:return []
        stk = []
        res = []
        for i in range(len(nums)):
            # 比当前元素小的数据都干掉
            while stk and nums[i]>nums[stk[-1]]:
                stk.pop()

            # # 超过窗口范围，队首元素出队
            while stk and i-k>=stk[0]:
                stk.pop(0)

            stk.append(i)
            # print(i, stk)
            if i+1>=k:
                res.append(nums[stk[0]])
        return res


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(Solution().maxSlidingWindow(nums, k))