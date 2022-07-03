"""
hard 2021-12-.... 区间dp（区间DP）（字节）
https://leetcode-cn.com/problems/minimum-cost-to-merge-stones/solution/yi-dong-you-yi-dao-nan-yi-bu-bu-shuo-ming-si-lu-he/
-
- i-j前缀的和为 nums[i...j]=sum[j]-sum[i-1]

"""
# dp[i,j]=所有将[i,j]合并为一堆的方案。
# 定义状态转移方程：最常见的写法为：
# dp[i,j] = max/min{dp[i,j], dp[i, k] + dp[k+1, j] + cost}。 ## 分界点k到底划还是不划
# 选取[i, j]之间的一个分界点k，分别计算[i, k]和[k+1, j]的最优解，从而组合出[i, j]的最优解。

# 枚举i为子区间左边界，枚举j为子区间有边界，枚举k为分界点。
# 要注意由于要求的是dp[1,n]，所以i必须从大往小遍历，j必须从小往大遍历。这样在状态转移方程中利用的就是已求解的dp状态。
class Solution:
    def mergeStones(self, stones, k):
        # 计算前缀和
        n = len(stones)
        preSum = [0 for _ in range(n+1)]
        # sum(i, j) = preSum[j + 1] - preSum[i]快速求区间和
        for i in range(n):
            preSum[i + 1] = preSum[i] + stones[i]
        # print(preSum) # [0, 3, 8, 9, 11, 17]

        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        # 至少要剩余2堆才能进行合并
        for x in range(2, n+1):

            for k in range(i, j):
                dp[i][j]=min(dp[i][j], dp[i][k]+dp[k+1][j]+sums[j]-sums[i-1])

if __name__ == '__main__':
    stones = [3,5,1,2,6]
    K = 3
    print(Solution().mergeStones(stones, K))
