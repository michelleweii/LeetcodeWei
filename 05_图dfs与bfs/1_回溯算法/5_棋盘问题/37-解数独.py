"""
hard 2021-10-18【回溯法】
1、排除已有元素
2、回溯所有可能
方块索引 = （行/3）*3 +列/3
填写（i，j）需要判断第i行有无这个元素；第j列有无这个元素；方块index里有无这个元素
row[1][2] = 1，表示第1行中2已经被使用
https://leetcode-cn.com/problems/sudoku-solver/solution/37-jie-shu-du-hui-su-sou-suo-suan-fa-xiang-jie-by-/
https://www.bilibili.com/video/BV1a4411k72j?spm_id_from=333.999.0.0
https://blog.csdn.net/qq_28410301/article/details/100560593
y总模板(详细)：https://www.acwing.com/solution/content/43802/
"""

class Solution:
    """
    bool backtracking(vector<vector<char>>& board) {
        for (int i = 0; i < board.size(); i++) {        // 遍历行
            for (int j = 0; j < board[0].size(); j++) { // 遍历列
                if (board[i][j] != '.') continue;
                for (char k = '1'; k <= '9'; k++) {     // (i, j) 这个位置放k是否合适
                    if (isValid(i, j, k, board)) {
                        board[i][j] = k;                // 放置k
                        if (backtracking(board)) return true; // 如果找到合适一组立刻返回
                        board[i][j] = '.';              // 回溯，撤销k
                    }
                }
                return false;                           // 9个数都试完了，都不行，那么就返回false
            }
        }
        return true; // 遍历完没有返回false，说明找到了合适棋盘位置了
    }
    """
    def __init__(self):
        self.sloved = 0
    def solveSudoku(self, board):
        # 初始化row、col、block[][]
        # 该位置已有元素，置1
        # 注意1-9，映射为0-8，num-1
        self.row = [[0 for _ in range(9)] for _ in range(len(board))]
        self.col = [[0 for _ in range(9)] for _ in range(len(board[0]))]
        self.block = [[0 for _ in range(9)] for _ in range(9)]
        # 初始化
        for i in range(len(board[0])):
            for j in range(len(board)):
                # 数独部分空格内已填入了数字，空白格用 '.' 表示。
                # 没有数据则不能初始化，跳过
                if board[i][j]=='.':continue
                index = (i//3)*3+j//3  # 9宫格对应哪一个
                num = int(board[i][j])
                self.row[i][num-1] = 1
                self.col[j][num-1] = 1
                self.block[index][num-1]=1
        # 回溯
        self.dfs(board, 0, 0)

    def dfs(self,board,i,j):
        # i行，j列
        # 整个9宫格便利结束
        if i==9:
            self.sloved = 1
            return
        # 如果该位置是数字
        if board[i][j]!='.':
            if j<8:self.dfs(board,i,j+1) # 向后移动一个格子
            else: self.dfs(board,i+1,0) # 下一行第一个格子开始
        else:
            index = (i//3)*3+j//3
            for k in range(9):
                # 如果数字k在行、列、块 中都没有使用
                if not self.row[i][k] and not self.col[j][k] and not self.block[index][k]:
                    board[i][j] = str(k+1) # 1-9填空，生成的是0-8
                    self.row[i][k] = 1
                    self.col[j][k] = 1
                    self.block[index][k] = 1
                    # 继续下一个
                    if j<8: self.dfs(board,i,j+1)
                    else:self.dfs(board,i+1,0)
                    # 如果没有解决，则回溯
                    if not self.sloved:
                        board[i][j] = '.'
                        self.row[i][k] = 0
                        self.col[j][k] = 0
                        self.block[index][k] = 0


if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(Solution().solveSudoku(board))
    print(board)
    # a = [0 for _ in range(9)]
    # print(a)