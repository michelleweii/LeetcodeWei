"""
middle 2021-11-08 二维动态规划
dp[i][j]: 到达网格(i,j)时, 共有 dp[i][j] 种走法。
https://leetcode-cn.com/problems/unique-paths/solution/62-bu-tong-lu-jing-tu-jie-dong-tai-gui-h-2b0k/
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for j in range(n)] for i in range(m)] # m*n
        # dp[0][0] = 1，从(0,0)到达(0,0)只有一条路径
        dp[0][0] = 1
        # 初始化 dp[0][j] 和 dp[i][0]
        # 边界，列
        for i in range(1, m):
            dp[i][0] = 1 # dp[i][0] = dp[i-1][0]+1
        # 边界，行
        for j in range(1, n):
            dp[0][j] = 1 # dp[0][j] = dp[0][j-1]+1

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]

        return dp[m-1][n-1] # return dp[-1][-1]

if __name__ == '__main__':
    m = 3
    n = 7
    print(Solution().uniquePaths(m,n))