"""
middle 2022-05-12 模拟题（不属于dfs or dfs）
https://leetcode-cn.com/problems/valid-sudoku/solution/36-jiu-an-zhao-cong-zuo-wang-you-cong-shang-wang-x/
"""
# i:在第 i 个行中是否出现过
# j:在第 j 个列中是否出现过
# j/3 + (i/3)*3: block中是否出现过
class Solution:
    def isValidSudoku(self, board):
        row = [{} for _ in range(9)]
        col = [{} for _ in range(9)]
        cell = [{} for _ in range(9)]
        n = len(board)
        for i in range(n):
            for j in range(n):
                block = j//3+3*(i//3)# 找单元
                num = board[i][j]
                if num != '.':
                    # // 遍历到第i行第j列的那个数, 我们要判断这个数在其所在的行有没有出现过，
                    # // 同时判断这个数在其所在的列有没有出现过
                    # // 同时判断这个数在其所在的box中有没有出现过
                    if num not in row[i] and num not in col[j] and num not in cell[block]:
                        # 之前都没出现过，现在出现了，就给它置为1，下次再遇见就能够直接返回false了
                        row[i][num] = 1
                        col[j][num] = 1
                        cell[block][num] = 1
                    else:
                        return False

        return True


if __name__ == '__main__':
    board=[
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(Solution().isValidSudoku(board))