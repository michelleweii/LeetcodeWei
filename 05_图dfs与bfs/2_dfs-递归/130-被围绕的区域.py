"""
middle 2021-08-25 dfs模板题
先从边界O开始，因为边界是不会被包围的，从边界的O开始dfs，遍历扩散到的都转为B；
遍历矩阵，将B都转为O，O都转为X
"""
# 被围绕的区间不会存在于边界上，换句话说，任何边界上的'O'都不会被填充为'X'。
# 任何不在边界上，或不与边界上的'O'相连的'O'最终都会被填充为'X'。
# 如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
class Solution:
    def solve(self, board) -> None:
        if not board or not board[0]:return board
        n, m = len(board), len(board[0])  # n行，m列
        # 从四周向内扩散
        # 左右（这块搞死了）
        for i in range(n):
            if board[i][0] == 'O':self.dfs(board, i, 0, n, m)
            if board[i][m-1] == 'O': self.dfs(board, i, m-1, n, m)
        # 上下（这块搞死了）
        for j in range(m):
            if board[0][j] == 'O': self.dfs(board, 0, j, n, m)
            if board[n-1][j] == 'O': self.dfs(board, n-1, j, n, m)

        print("扩散结果：", board)
        # 再次遍历board，将所有的Y转为O，其余所有转为X
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'Y':board[i][j] = 'O'
                else: board[i][j] = 'X'
        print("最终结果：", board)

    def dfs(self,board,x,y,n,m):
        # 定义出口 ???
        board[x][y] = 'Y'
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        # 从当前位置(x,y)的4个方向开始遍历
        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if a>=0 and a<n and b>=0 and b<m and board[a][b]=='O':
                self.dfs(board,a,b,n,m)


if __name__ == '__main__':
    board = [['X', 'X', 'X', 'X'],
             ['X', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'X']]
    print(Solution().solve(board))
"""
[["X","X","X","X"],
["X","X","X","X"],
["X","X","X","X"],
["X","O","X","X"]]
"""