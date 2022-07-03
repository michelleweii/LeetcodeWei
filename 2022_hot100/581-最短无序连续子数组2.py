"""
middle 2021-12-15 单调栈
题目：找出一个 连续子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序
连续子数组：要求下标连续
解法一：单调栈：寻找起点和终点
https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/solution/dan-diao-zhan-jie-fa-by-lilin-k-7096/
https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/solution/dan-diao-zhan-jie-fa-on-by-20182726-e3pb/

解法二：双指针 + 线性扫描
https://www.bilibili.com/video/BV1yK4y1Q7QT
"""
class Solution:
    # 单调栈!!! 【核心】
    # 正序遍历，找比cur值小(找与题意相反，即不符合)，单调递增栈
    # 逆序遍历，找比cur值大，单调递减栈
    def findUnsortedSubarray_stk(self, nums):
        n = len(nums)
        stk = []
        left, right = n, 0 # 设置一个取不到的值即可
        # 1、正序遍历，单调递增栈
        for i in range(n):
            while stk and nums[i]<nums[stk[-1]]:
                # 具体操作
                # print(stk[-1])
                left = min(left, stk[-1])
                stk.pop()
            stk.append(i)
        # 2、逆序遍历，单调递减栈
        # print('stk', stk)
        for i in range(n-1, -1, -1):
            while stk and nums[i]>nums[stk[-1]]:
                # 具体操作
                right = max(right, stk[-1])
                stk.pop()
            stk.append(i)

        return max(0, right - left + 1)

    # 指针 + 线性扫描
    def findUnsortedSubarray(self, nums): #List[int]) -> int:
        n = len(nums)
        max_value, min_value = float('-inf'), float('inf')
        left,right = 0, n-1
        # 从前向后找，找到不符合递增元素的下标
        for i in range(n):
            if nums[i]>=max_value:
                max_value = nums[i]
            else:
                left = i
        # 从后向前找，找到不符合递减元素的下标
        for j in range(n-1, -1, -1):
            if nums[j]<=min_value:
                min_value = nums[j]
            else:
                right = j

        if left==0 and right==n-1:
            return 0
        # print(left,right)
        return left-right+1



if __name__ == '__main__':
    nums = [2, 6, 4, 8, 10, 9, 15] # 5
    # nums = [1]
    # print(Solution().findUnsortedSubarray(nums))
    print(Solution().findUnsortedSubarray_stk(nums))