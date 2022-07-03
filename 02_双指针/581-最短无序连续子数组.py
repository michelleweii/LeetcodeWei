"""
middle 2021-12-15 双指针
题目：找出一个 连续子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序
连续子数组：要求下标连续
解法二：双指针 + 线性扫描
https://www.bilibili.com/video/BV1yK4y1Q7QT
(this)https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/solution/si-lu-qing-xi-ming-liao-kan-bu-dong-bu-cun-zai-de-/
https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/solution/gong-shui-san-xie-yi-ti-shuang-jie-shuan-e1le/

解法一：单调栈：寻找起点和终点
https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/solution/dan-diao-zhan-jie-fa-by-lilin-k-7096/
"""
class Solution:
    # 指针 + 线性扫描
    # 时间复杂度：O(n)
    # https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/solution/si-lu-qing-xi-ming-liao-kan-bu-dong-bu-cun-zai-de-/
    def findUnsortedSubarray(self, nums): #List[int]) -> int:
        n = len(nums)
        max_value, min_value = float('-inf'), float('inf')
        left, right = 0, n-1
        # 从前向后找，找到不符合递增元素的下标
        for i in range(n):
            if nums[i]>=max_value:
                max_value = nums[i]
            else:
                left = i # 最后一个，left=5
        # 从后向前找，找到不符合递减元素的下标
        for j in range(n-1, -1, -1):
            if nums[j]<=min_value:
                min_value = nums[j]
            else:
                right = j

        # 是递增的
        if left==0 and right==n-1:
            return 0
        # print(left,right)
        return left-right+1

    # 双指针+排序 时间复杂度：O(nlogn)
    # 先将数组拷贝一份进行排序，然后使用两个指针 i 和 j 分别找到左右两端第一个不同的地方，
    # 那么 [i, j] 这一区间即是答案。
    def sortarr(self, nums):
        n = len(nums)
        arr = nums.copy()
        arr.sort()
        i, j = 0, n-1
        while i<=j and nums[i]==arr[i]:i+=1
        while i<=j and nums[j]==arr[j]:j-=1
        return j-i+1

    # 单调栈
    # def findUnsortedSubarray_stk(self, nums):
    #     n = len(nums)
    #     stk = []
    #     res = 0
    #     for i in range(n):
    #         while stk and nums[i]>nums[stk.pop()]:
    #             # 具体操作
    #
    #         stk.append(i)
    #
    #     return res

if __name__ == '__main__':
    nums = [2, 6, 4, 8, 10, 9, 15] # [6, 4, 8, 10, 9], 5
    # nums = [1] # 0
    print(Solution().findUnsortedSubarray(nums))