
# 2022-02-28
class Solution:
    def minimumTotal(self, triangle):
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
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print(Solution().minimumTotal(triangle))