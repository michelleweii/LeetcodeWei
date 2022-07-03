"""
middle 2022-01-25 【单调递增栈】
https://leetcode-cn.com/problems/maximum-subarray-min-product/solution/python-qian-zhui-he-dan-diao-zhan-qing-x-gow8/
题目：最小乘积的最大值由子数组 [2,3,2]（最小值是 2）得到。
2 * (2+3+2) = 2 * 7 = 14 。
"""
class Solution:
    def maxSumMinProduct(self, nums):  #List[int]) -> int:
        nums = [0]+nums+[0] # 添加哨兵, 方便单调栈内的判断
        # 前缀和
        presum = [0]
        for n in nums:
            presum.append(presum[-1] + n)
        print(presum) # [0, 0, 1, 3, 6, 8, 8]
        # print(presum[4]-presum[2])
        res = 0
        # 找右边第一个比它小的元素下标、左边第一个比它小的元素下标
#       在构建单调栈的过程中计算的方法。stk.top()所在子数组最小值是它自己，
#       最右是马上要进栈的那个值的左边一格，最左是stk.top()出栈后的栈顶的右边一格。
        # 求以stk.top()为矮柱的面积
        stk = []
        for i in range(len(nums)):
            while stk and nums[stk[-1]]>nums[i]: # 单调递增栈
                cur_tmp = nums[stk[-1]] # 当前元素
                # 当前元素右边最小值 i
                stk.pop()
                # 当前元素左边最小值 stk[-1]
                res = max(res, cur_tmp * (presum[i]-presum[stk[-1]+1]) )
                # print(cur_tmp, i, stk[-1]) #2 5 1
                # w: i-stk[-1]-1
                # 前缀和,求nums[i]~nums[j]的前缀和presum[j+1]-presum[i]
                # 本题区间是cur到最左元素+1，所以缩小范围得到 presum[i]-presum[stk[-1]+1]
            stk.append(i)

        return res % 1000000007


if __name__ == '__main__':
    nums = [1, 2, 3, 2]
    print(Solution().maxSumMinProduct(nums))