
# 2022-02-28
class Solution:
    def maximalSquare(self, matrix) -> int:
        if not len(matrix) or not len(matrix[0]):return 0
        m,n = len(matrix),len(matrix[0])
        # # 状态定义：dp[i][j]表示以matrix[i][j]为右下角，所构成的最大边长
        dp = [[0] * n for _ in range(m)]

        # 初始化
        max_side = 0
        for i in range(n):
            dp[0][i] = int(matrix[0][i])
            max_side = dp[0][i] if max_side<dp[0][i] else max_side
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            max_side = dp[i][0] if max_side < dp[i][0] else max_side


        for i in range(1, m):
            for j in range(1,n):
                if matrix[i][j]=='1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
                    max_side = max(max_side, dp[i][j])
        return max_side*max_side



if __name__ == '__main__':
    # matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
    #           ["1", "0", "0", "1", "0"]] # 4
    # matrix = [["0", "1"], ["1", "0"]] # 1
    matrix = [["0"],["1"]] # 1
    print(Solution().maximalSquare(matrix))