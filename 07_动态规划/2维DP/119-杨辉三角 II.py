"""
easy 2021-12-07 二维dp基础题
左对齐，dp[i][j]=dp[i][j-1]+dp[i-1][j-1]
注意遍历条件
"""
class Solution:
    def getRow(self, rowIndex: int):
        # 定义二维dp
        dp = [[0]*(rowIndex+1) for _ in range(rowIndex+1)]
        dp[0][0] = 1

        for i in range(1, rowIndex+1):
            rowlist = []
            for j in range(i+1): # j<=i
                if j==0: dp[i][j] = 1
                else:dp[i][j] = dp[i-1][j] + dp[i-1][j-1] # 状态转移方程

                rowlist.append(dp[i][j]) # 每行的结果
        return dp[-1]
        # print(dp[-1])

if __name__ == '__main__':
    rowIndex = 3
    print(Solution().getRow(rowIndex))