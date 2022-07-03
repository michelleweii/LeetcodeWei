"""
middle 2022-05-31 序列dp
[理论]https://leetcode.cn/problems/knight-probability-in-chessboard/solution/gong-shui-san-xie-jian-dan-qu-jian-dp-yu-st8l/
[code]https://leetcode.cn/problems/knight-probability-in-chessboard/solution/pythonjavajavascriptgo-dong-tai-gui-hua-2ij3m/
状态定义：dp[i][j][p] 为从位置 (i,j) 出发，使用步数不超过 p 步，最后仍在棋盘内的概率。
初始化，p=0，一步也不走，100%落在棋盘内。
状态转移: dp[x][y][p-1]*(1/8), 因为有8个方向，1个方向贡献的概率要*(1/8)
"""
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int):# -> float:
        dp= [[[0] * (k + 1) for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                dp[i][j][0]=1

        dx=[-1,-1,-2,-2,1,1,2,2]
        dy=[2,-2,1,-1,2,-2,1,-1]

        for p in range(1,k+1):
            for i in range(n):
                for j in range(n):
                    for d in range(8):
                        nx=i+dx[d]
                        ny=j+dy[d]
                        if nx<0 or nx>=n or ny<0 or ny>=n:continue
                        dp[i][j][p]+=dp[nx][ny][p-1]*1.0/8
        return dp[row][column][k]


if __name__ == '__main__':
    n = 3
    k = 2
    row = 0
    column = 0
    print(Solution().knightProbability(n,k,row,column))