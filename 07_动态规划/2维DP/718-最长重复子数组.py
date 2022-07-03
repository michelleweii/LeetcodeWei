"""
middle 2022-03-03 二维dp
https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/solution/zhe-yao-jie-shi-ken-ding-jiu-dong-liao-by-hyj8/
"""
class Solution:
    def findLength(self, nums1, nums2):
        if not nums1 or not nums2:return 0
        res = 0

        lens1, lens2=len(nums1), len(nums2)
        # dp[i][j]表示，nums1[0,i-1]和nums2[0,j-1]所构成的 公共的 、长度最长的子数组的长度。
        dp = [[0]*(lens1+1) for _ in range(lens2+1)] # 这里注意先后顺序，先列后行

        # 状态转移
        for i in range(1, lens1+1):
            for j in range(1, lens2+1):
                if nums1[i-1]==nums2[j-1]:
                    # print('nums1[i-1]',nums1[i-1])
                    dp[i][j] = dp[i-1][j-1]+1
                    res = max(res,dp[i][j])

        return res

if __name__ == '__main__':
    nums1 = [1, 2, 3, 2, 1]
    nums2 = [3, 2, 1, 4, 7]
    # 输出：3
    # 解释：长度最长的公共子数组是 [3,2,1] 。
    print(Solution().findLength(nums1,nums2))