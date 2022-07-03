"""
easy 模拟题
2021-07-15
https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/solution/mian-shi-ti-29-shun-shi-zhen-da-yin-ju-zhen-she-di/
"""
class Solution:
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]: return matrix
        res = []
        n = len(matrix)
        m = len(matrix[0])
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        x,y,d = 0,0,1
        visited = [[False for _ in range(m)] for _ in range(n)]
        for i in range(n*m):
            res.append(matrix[x][y])
            visited[x][y] = True
            a = x+dx[d]
            b = y+dy[d]
            if a<0 or a>=n or b<0 or b>=m or visited[a][b]:
                d = (d+1)%4
                a = x + dx[d]
                b = y + dy[d]
            x = a
            y = b
        return res

if __name__ == '__main__':
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(Solution().spiralOrder(matrix))



