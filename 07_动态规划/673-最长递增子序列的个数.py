"""
middle 2022-01-24 序列dp
https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/solution/dai-ma-sui-xiang-lu-dai-ni-xue-tou-dp673-9txt/
https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/solution/gong-shui-san-xie-lis-de-fang-an-shu-wen-obuz/
# lc300是求最长上升子序列的长度是是多少，是求len
# 这道题是求最长上升子序列那个最长的那个一共有多少个，多少组，有多少个可能性构成。
【状态定义】
1. dp[i]：以 `nums[i]` 结尾的最长递增子序列长度；
2. count[i]：以`nums[i]`为结尾的字符串，最长递增子序列的个数；
"""
# 【本题重点】分情况讨论
# 1. dp[i] < dp[j]+1 # 最长递增子序列长度++，说明找到了一个更长的递增子序列。
# 说明 dp[i]会被 dp[j]+1 直接更新，此时同步直接更新 cnt[i] = cnt[j] 即可；
# ???
# 2. dp[i] = dp[j]+1 # 说明找到了两个相同长度的递增子序列。
# 说明找到了一个新的符合条件的前驱，此时将值继续累加到方案数当中，即有 cnt[i] += cnt[j]。
# ???
class Solution:
    def findNumberOfLIS(self, nums):
        res = 0
        max_len = 1
        # dp[i]是以第i个元素结尾的最长递增子序列的长度
        dp = [1 for _ in range(len(nums))]
        # 每个递增序列对应的子序列的个数
        cnt = [1 for _ in range(len(nums))]
        for i in range(1,len(nums)):
            for j in range(i):
                # 更新最长递增子序列长度
                # 说明找到了一个更长的递增子序列
                if nums[i]>nums[j] and dp[i] < dp[j]+1:
                        dp[i] = dp[j]+1
                        cnt[i] = cnt[j] # 【Attention】
                # 更新最长递增子序列个数
                # 说明找到了两个相同长度的递增子序列
                elif nums[i]>nums[j] and dp[i] == dp[j]+1:
                    # print(i,j, dp[i], dp[j]+1) # 4 3 4 4
                    cnt[i] += cnt[j]
                    # 【Attention】
                    # [1,3,5], 以nums[2]为结尾的LIS，那么cnt[2]=1
                    # [1,3,4], 以nums[3]为结尾的LIS，那么cnt[3]=1
                    # 所以 cnt[4] = cnt[4]+cnt[3] = 2， 以nums[4]为结尾的最大个数
                    # 有2个状态可以转换过来
            max_len = max(max_len,dp[i]) # 最长递增子序列的长度

        print('dp', dp) # dp [1, 1, 1, 1, 1]
        print('cnt', cnt) # cnt [1, 1, 1, 1, 1]
        for k in range(len(nums)):
            # 以nums[k]结尾的最长递增子序列长度
            if dp[k] == max_len:
                res += cnt[k]
        return res

if __name__ == '__main__':
    # nums = [2,2,2,2,2]
    nums = [1,3,5,4,7]
    print(Solution().findNumberOfLIS(nums))
    # print(Solution().fn(nums))
