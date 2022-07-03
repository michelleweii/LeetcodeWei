"""
easy 2022-01-22 dp
# 注意这道题，不是选nums[i] or 不选nums[i]
# 状态定义：`dp[i]`表示以 `nums[i]` 结尾 的 连续 子数组的最大和。
# 转移方程：根据状态的定义，由于 `nums[i]` 一定会被选取。`dp[i-1]` 有可能是负数，
# 所以问题转为`dp[i-1]`选or不选。
"""
# list的每个位置都保留到目前位置，list的最大的和。
# 进阶LC918
class Solution(object):
    def maxSubArray(self, nums):
        # 选dp[i-1]+nums[i]
        # 不选nums[i]
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        res = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
            res = max(res, dp[i])
        # return max(dp)
        return res

def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    myResult = Solution()
    print(myResult.maxSubArray(nums))


if __name__ == '__main__':
    main()
