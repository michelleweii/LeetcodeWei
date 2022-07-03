"""
easy 一维dp
2021-07-15 once ok
"""
class Solution:
    # dp[i] 以i结尾的连续子数组的最大和
    def maxSubArray(self, nums) -> int:
        n = len(nums)
        dp = [0 for _ in range(n)]
        for i in range(n):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
        # print(dp)
        return max(dp)

if __name__ == '__main__':
    # nums = [-2,1,-3,4,-1,2,1,-5,4]
    nums = [-2,1,-3]
    print(Solution().maxSubArray(nums))