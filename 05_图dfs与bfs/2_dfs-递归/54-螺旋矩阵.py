"""
middle 2022-01-18 类似dfs遍历的模拟
https://www.acwing.com/solution/content/15338/ 扩散方向
【核心】检验下一个位置是否合法, 不合法则更新方向, 并重新计算下一个位置
坐标轴
x<---
    |
    y
"""
class Solution:
    # 模板解法
    def spiralOrder(self, matrix):
        res = []
        if not matrix or not matrix[0]:return res
        m = len(matrix)
        n = len(matrix[0])
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        used = [[False for _ in range(n)] for _ in range(m)]

        # 初始化
        x, y = 0, 0 # 一开始的位置
        d = 0 # 一开始的方向
        for i in range(m*n):
            res.append(matrix[x][y])
            used[x][y] = True

            # 检验下一个位置是否合法, 不合法则更新方向, 并重新计算下一个位置
            a = x+dx[d]
            b = y+dy[d]
            if a<0 or a>=m or b<0 or b>=n or used[a][b]:
                d += 1
                d %= 4 # 不合法重新更新起点

                a = x + dx[d]
                b = y + dy[d]

            x = a
            y = b

        return res


    # def spiralOrder(self, matrix):
    #     res = []
    #     row = len(matrix)
    #     col = len(matrix[0])
    #     x1,y1 = 0,0
    #     x2,y2 = row-1,col-1
    #     while x1 <= x2 and y1 <= y2:
    #         # print(x1,y1)
    #         for i in range(x1, x2+1):
    #             res.append(martix[y1][i])
    #             # print(martix[y1][i])
    #
    #         for j in range(y1+1,y2+1):
    #             res.append(martix[j][x2])
    #             # print(martix[j][x2])
    #         # print(x2,y2)
    #         # print('-----')
    #         if x1<x2 and y1<y2:
    #             for i in range(x2-1,x1,-1):
    #                 res.append(martix[y2][i])
    #                 # print(martix[y2][i])
    #             # print('------')
    #             for j in range(y2,y1,-1):
    #                 res.append(martix[j][x1])
    #                 # print(martix[j][x1])
    #
    #         x1 += 1
    #         y1 += 1
    #         x2 -= 1
    #         y2 -= 1
    #
    #     return res

if __name__ == '__main__':
    martix = [
             [ 1, 2, 3 ],
             [ 4, 5, 6 ],
             [ 7, 8, 9 ]
            ]
    print(Solution().spiralOrder(martix))