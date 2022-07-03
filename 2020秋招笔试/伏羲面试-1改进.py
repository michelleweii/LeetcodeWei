class Solution:
    def updateMatrix(self, matrix):
        res = []
        if not matrix or not matrix[0]:return res
        m, n = len(matrix), len(matrix[0])
        queue = []
        visited = set()
        # 初始化队列，将所有起始点都加入
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    queue.append((i,j))
                    visited.add((i,j))
        while queue:
            a,b = queue.pop(0)
            dx = [-1,0,1,0]
            dy = [0,1,0,-1]
            for i in range(4):
                x = a+dx[i]
                y = b+dy[i]
                # 如果没有撞墙，就添加
                if x>=0 and x<m and y>=0 and y<n and (x,y) not in visited:
                    queue.append((x,y))
                    visited.add((x,y))
                    matrix[x][y] = matrix[a][b]+1 # 注意这里是修改了原数组
        return matrix

if __name__ == '__main__':
    matrix = [[0, 0, 0],[0, 1, 0],[1, 1, 1]]
    print(Solution().updateMatrix(matrix))




