"""
middle 2维DP
2021-07-18
"""
# 设 f(i, j)n为从棋盘左上角走至单元格 (i,j) 的礼物最大累计价值
class Solution:
    def maxValue(self, grid):
        if not grid and not grid[0]:return 0
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # 初始化
        dp[0][0] = grid[0][0]
        for i in range(1,m):
            dp[i][0] = dp[i-1][0]+grid[i][0]
        for j in range(1,n):
            dp[0][j] = dp[0][j-1]+grid[0][j]
        # print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[m-1][n-1]

if __name__ == '__main__':
    grid = [
              [1,3,1],
              [1,5,1],
              [4,2,1]
            ]
    print(Solution().maxValue(grid))