"""
middle 2021-12-14 2维DP
题目：求自顶向下的最小路径和。定义dp[i][j]为从点(i,j)到底边的最小路径和
[i,j]
[i+1,j] [i+1,j+1]
https://leetcode-cn.com/problems/triangle/solution/di-gui-ji-yi-hua-dp-bi-xu-miao-dong-by-sweetiee/
需要注意的是，从下到上，那么dp[i]由dp[i+1]转化而来！！！
"""
class Solution(object):
    def minimumTotal(self, triangle):
        m = len(triangle) # m行m列
        dp = [[0]*(m+1) for _ in range(m+1)] # (i,j)点到底边的最小路径和
        # 初始化边界
        # for j in range(m):
        #     dp[m-1][j] = triangle[m-1][j] # 但是triangle没有index=4
        for i in range(m-1, -1, -1):
            for j in range(i, -1, -1):
                # 到达[i,j]的最短路径
                dp[i][j] = min(dp[i+1][j],dp[i+1][j+1])+triangle[i][j]
        ## 从三角形的最后一行开始递推，如下循环也ok
        # for (int i = n - 1; i >= 0; i--) {
        #     for (int j = 0; j <= i; j++) {
        return dp[0][0]

    # 2022-02-28
    def minimumTotal_mine(self, triangle):
        if not triangle and not triangle[-1]:return 0

        m,n=len(triangle),len(triangle[-1])
        dp = [[0]*n for _ in range(m)]

        for i in range(n):
            dp[m-1][i] = triangle[m-1][i]

        for i in range(m-2,-1,-1): # m行n列
            for j in range(n-1,-1,-1):
                if j>i:continue
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1])+triangle[i][j]
        return dp[0][0]

if __name__ == '__main__':
    # triangle = [[-10]]
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# [2]
# [3, 4]
# [6, 5, 7]
# [4, 1, 8, 3]
    print(Solution().minimumTotal(triangle))