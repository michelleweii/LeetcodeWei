"""
middle 2022-02-24 dfs
【求最大连通图面积】https://leetcode-cn.com/problems/max-area-of-island/solution/dao-yu-de-zui-da-mian-ji-jian-dan-de-di-gui-tu-jie/
注意和【求连通图数量】不一样，LC200岛屿数量。
"""
class Solution:
    def maxAreaOfIsland(self, grid): #List[List[int]]) -> int:
        if not len(grid) or not len(grid[0]):return 0
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = self.dfs(grid, i, j)
                    max_area = max(max_area, area)
        return max_area

    def dfs(self, grid, x, y):
        area = 1 # 只要进dfs，面积就是1
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        grid[x][y] = 0 # 沉岛思想
        for d in range(4):
            a = x+dx[d]
            b = y+dy[d]
            if a>=0 and a<len(grid) and b>=0 and b<len(grid[0]) and grid[a][b]==1:
                area += self.dfs(grid, a, b)
        return area


if __name__ == '__main__':
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    # # 6
    # grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
    # 4
    print(Solution().maxAreaOfIsland(grid))