"""
middle 2019-08-29 BFS模板遍历（网易校招原题）——【最短路径】
https://leetcode-cn.com/problems/01-matrix/solution/2chong-bfs-xiang-jie-dp-bi-xu-miao-dong-by-sweetie/
题目：求每个元素与最近0的距离。
【为什么只能用BFS?】
所有为0点入队列，一个个弹出，可以找到所有最短距离为1的节点，
此时再一个个弹出最短距离为1的节点，可以找到所有最短距离为2的节点，循环往复...
https://leetcode-cn.com/problems/01-matrix/solution/python-bfs-by-qinyu-c-azzt/

# 2022-05-12 回顾，完全忘记了
# 从0开始向外扩散
1、将所有的0入队；从0开始向四周扩散；能扩散到的位置说明距离0的distance=1；
2、将所有的1入队；从1开始向四周扩散；能扩散到的位置说明距离0的distance=2；
"""
class Solution:
    def updateMatrix(self, matrix):
        res = []
        if not matrix or not matrix[0]:return res
        m, n = len(matrix), len(matrix[0])
        queue = []
        visited = set()
        # 初始化队列，将所有为0的起始点都加入
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
                    # 扩散前点 matrix[a][b]
                    # 扩散后点 matrix[x][y]
                    matrix[x][y] = matrix[a][b]+1 # 注意这里是修改了原数组【妙妙妙】
        return matrix

if __name__ == '__main__':
    matrix = [[0, 0, 0],[0, 1, 0],[1, 1, 1]]
    print(Solution().updateMatrix(matrix))