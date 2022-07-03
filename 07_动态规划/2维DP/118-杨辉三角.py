"""
easy 2021-12-07 二维dp基础题
左对齐，dp[i][j]=dp[i][j-1]+dp[i-1][j-1]
注意遍历条件
https://leetcode-cn.com/problems/pascals-triangle/solution/zui-tong-su-yi-dong-de-dong-tai-gui-hua-7gsoa/
"""
class Solution:
    def generate(self, numRows: int):
        res = []
        # 定义二维dp
        dp = [[0]*numRows for _ in range(numRows)]
        dp[0][0] = 1
        res.append([1])

        for i in range(1, numRows):
            rowlist = []
            for j in range(i+1): # j<=i
                if j==0: dp[i][j] = 1
                else:dp[i][j] = dp[i-1][j] + dp[i-1][j-1] # 状态转移方程

                rowlist.append(dp[i][j]) # 每行的结果

            res.append(rowlist) #

        return res

if __name__ == '__main__':
    numRows = 5
    print(Solution().generate(numRows))