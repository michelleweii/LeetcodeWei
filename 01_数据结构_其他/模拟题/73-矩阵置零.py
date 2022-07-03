"""
middle 2021-11-08
如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0.
思路：用 O(1) 空间
关键思想: 用matrix第一行和第一列记录该行该列是否有0,作为标志位
https://leetcode-cn.com/problems/set-matrix-zeroes/solution/o1kong-jian-by-powcai/
简化版看不懂=.=
"""
class Solution:
    # 两遍扫matrix,第一遍用集合记录哪些行,哪些列有0;第二遍置0
    # 用 O(m+n) 额外空间
    def setZeroes_mn(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        row_zero = set()
        col_zero = set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    row_zero.add(i)
                    col_zero.add(j)
        for i in range(row):
            for j in range(col):
                if i in row_zero or j in col_zero:
                    matrix[i][j] = 0

    def setZeroes(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        row0_flag = False
        col0_flag = False
        # 找第一行是否有0
        for j in range(col):
            if matrix[0][j] == 0:
                row0_flag = True
                break
        # 第一列是否有0
        for i in range(row):
            if matrix[i][0] == 0:
                col0_flag = True
                break
        # 把第一行或者第一列作为 标志位
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        # 矩阵置0
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if row0_flag:
            for j in range(col):
                matrix[0][j] = 0
        if col0_flag:
            for i in range(row):
                matrix[i][0] = 0

if __name__ == '__main__':
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    print(Solution().setZeroes_mn(matrix))
    print(Solution().setZeroes(matrix))