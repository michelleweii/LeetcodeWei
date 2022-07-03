"""
middle 2021-11-08 二维动态规划
每次只能向下或者向右移动一步。
https://leetcode-cn.com/problems/unique-paths-ii/solution/jian-dan-dpbi-xu-miao-dong-by-sweetiee/
dp[i,j]表示从(0,0)走到(i,j)的所有不同路径的方案数。
重点：如果网格 (i, j) 上有障碍物，则 dp[i][j] 值为 0，表示走到该格子的方案数为 0；
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        if not obstacleGrid or not obstacleGrid[0]:return 0
        if obstacleGrid[0][0] == 1: return 0 # 对dp[0][0]进行障碍物判断
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        # 这里有不同，如果该位置是障碍物，则dp[0][0]=0
        dp[0][0] = 1 # dp[0][0] = 1，从(0,0)到达(0,0)只有一条路径
        # 初始化 dp[0][j] 和 dp[i][0]
        """
        # 我之前这样赋值是有问题的，第一行第一列初始化应该考虑到上一个状态，
        # 比如第一行dp[0][i] = dp[0][i-1]，
        # 因为前一个格子到不了的情况下当前格子也到不了
        # java可以在for里限制条件，比如 for (int i = 0; i < m && obstacleGrid[i][0] == 0; i++) 
        # java：for 循环中的condition 为true 才会继续循环， 为false 则直接跳出循环。
        # 所以一旦遇到值为1的情况，后面的都不会被赋值成1。但是！python不是!
----------------------------------------------------------------------------------    
        # 边界，行
        for i in range(m):
            dp[i][0] = 1 if obstacleGrid[i][0]==0 else 0
        # 边界，列
        for j in range(n):
            dp[0][j] = 1 if obstacleGrid[0][j] == 0 else 0
        """
        # 对行赋值
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i - 1][0]
        # 对列赋值
        for j in range(1, n):
            dp[0][j] = 0 if obstacleGrid[0][j] == 1 else dp[0][j - 1]

        # 状态转移
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==0:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]

        return dp[m-1][n-1] # return dp[-1][-1]

if __name__ == '__main__':
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]] # 2
    # obstacleGrid = [[1,0]] # 0
    print(Solution().uniquePathsWithObstacles(obstacleGrid))
