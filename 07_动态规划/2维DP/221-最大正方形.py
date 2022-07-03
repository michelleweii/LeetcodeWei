"""
middle 2021-12-13 2维DP
题目：在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
定义：用dp(i,j)表示以(i,j)为右下角，且只包含 1 的正方形的边长最大值。

核心：若某格子值为 1，则以此为右下角的正方形的、最大边长为：上面的正方形、左面的正方形或左上的正方形中，最小的那个，再加上此格。
https://leetcode-cn.com/problems/maximal-square/solution/li-jie-san-zhe-qu-zui-xiao-1-by-lzhlyle/
"""
class Solution:
    def maximalSquare(self, matrix): #List[List[str]]) -> int:
        if not matrix or not matrix[0]:return 0
        m = len(matrix)
        n = len(matrix[0])
        if m == 0 or n == 0:
            return 0
        dp = [[0 for i in range(n)] for j in range(m)]
        maxSize = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1': # 这个位置等于1才有计算的必要
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]) + 1
                maxSize = max(dp[i][j], maxSize)
        return maxSize * maxSize

if __name__ == '__main__':
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]

    print(Solution().maximalSquare(matrix))