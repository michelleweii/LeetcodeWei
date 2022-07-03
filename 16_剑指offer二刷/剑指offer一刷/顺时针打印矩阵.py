# -*- coding:utf-8 -*-
import numpy as np
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res = []
        if not matrix: return res
        n = len(matrix) # n行
        m = len(matrix[0]) # m列
        # visted = # 记录是否被访问过
        # for i in range(m):
        #     aa.append(False)
        # print(aa)
        # for j in range(n):
        #     visted.append(aa)  # 这种初始化方式就是错的
        visted = [[False for _ in range(m)] for _ in range(n)]
        # print(visted)
        x,y = 0,0 # 第一个点
        d = 1 # 初始方向是向右
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        for i in range(n*m):
            res.append(matrix[x][y])
            visted[x][y] = True
            a = x + dx[d]
            b = y + dy[d]
            if a<0 or a>=n or b<0 or b>=m or visted[a][b]:
                # 撞墙啦！ 就换方向
                d = (d+1)%4
                a = x + dx[d]
                b = y + dy[d]
            x, y = a, b
        return res



if __name__ == '__main__':
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    matrix = [[1],[2],[3],[4],[5]]
    matrix = [[1,2],[3,4]]
    # print(matrix[0][0])
    # aa = [[False for j in range(4)] for i in range(3)]
    # print(aa)
    # print(visted)
    print(Solution().printMatrix(matrix))