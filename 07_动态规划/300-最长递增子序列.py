"""
middle 2021-12-08 一维dp->扩展题LC673
状态定义：dp[i] 的值代表 nums 以 nums[i] 结尾的最长子序列长度。
数组：要求连续i-1,i,i+1
子序列：不要求连续i-3,i,i+5
https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-dong-tai-gui-hua-2/
"""
# 我的疑问？为什么不能只判断前一位？而是要判断前面的所有位？
# 因为题目是子序列，不要求下标连续！！！

# max也不能少！为啥呢?
# 因为在遍历[0,j)的时候，dp[i]的值会一直变化，如果不加max，则dp[i]一定等于最后一个状态j的值+1；
# 但是此刻状态不一定是最大的。
class Solution:
    def lengthOfLIS(self, nums):
        if len(nums)==0:return 0
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                # 当前元素要比之前的元素大，才可以跟在后面，构成上升
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i], dp[j]+1) # dp[j] 是之前元素的最大值
        return max(dp)

if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(Solution().lengthOfLIS(nums))


