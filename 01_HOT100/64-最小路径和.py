"""
middle 2022-05-13 dp
# 设dp[i][j]为到达位置（i，j）时的最优解
"""
# 请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
class Solution(object):
    def func(self,grid):
        m,n=len(grid),len(grid[0])
        # dp[i][j]表示i,j位置最小路径和
        dp=[[0]*n for _ in range(m)]
        dp[0][0]=grid[0][0]
        for i in range(1,m):
            dp[i][0]=dp[i-1][0]+grid[i][0]
        for j in range(1,n):
            dp[0][j]=dp[0][j-1]+grid[0][j]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]

        return dp[-1][-1]

    def minPathSum(self, grid):
        # 设dp[i][j]为到达位置（i，j）时的最优解
        dp = [[0 for col in range(len(row))] for row in grid]
        row = len(grid)
        col = len(grid[0])
        # print(dp)
        # row = [0]*len(grid)
        # print(row)
        # dp2 = [row]*len(grid)
        # print(dp2) # 同样可以到达列表生成式的效果，但是这种会改变！
        # 对第一行进行初始化
        dp[0][0] = grid[0][0]
        for j in range(1,len(grid[0])):
            dp[0][j] = dp[0][j-1]+grid[0][j]
        # print(dp[0])
        # 对第一列进行初始化
        for i in range(1,len(grid)):
            dp[i][0] = dp[i-1][0]+grid[i][0]
        # for i in range(3):
        #     print(dp[i][0])
        # DP构建矩阵
        for i in range(1,len(grid)):
            for j in range(1,len(grid[i])):
                dp[i][j]=min(dp[i-1][j]+grid[i][j],dp[i][j-1]+grid[i][j])

        # print(dp[row-1][row-1])
        # 最右下角保存的是最小路径和
        return dp[row-1][col-1]


if __name__ == '__main__':
    grid =[
        [1,3,1],
        [1,5,1],
        [4,2,1]
    ]
    print(Solution().minPathSum(grid))