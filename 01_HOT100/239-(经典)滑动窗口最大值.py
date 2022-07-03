"""
hard 2021-10-27【单调递减栈】
"""
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        res = []
        if not nums or not k:return res
        q = [] # 存的是下标
        for i in range(len(nums)):
            # 维护递增队列，比队尾大的才插入
            # 把比当前插入元素小的都干掉
            while q and nums[i]>nums[q[-1]]:
                q.pop()
            q.append(i)

            while q and i - k >= q[0]:
                q.pop(0)  # 超过窗口范围，队首元素出队

            # 每次返回队头元素
            if i+1>=k:res.append(nums[q[0]])
        return res


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    print(nums.pop()) # 7
    k = 3
    # [3,3,5,5,6,7]
    res = Solution()
    print(res.maxSlidingWindow(nums, k))