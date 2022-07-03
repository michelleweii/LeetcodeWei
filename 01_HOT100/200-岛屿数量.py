"""
middle 2021-08-25 bfs/dfs 遍历模板题（回溯，四个方向不断尝试）
https://leetcode-cn.com/problems/number-of-islands/solution/dao-yu-lei-wen-ti-de-tong-yong-jie-fa-dfs-bian-li-/
https://leetcode-cn.com/problems/number-of-islands/solution/number-of-islands-shen-du-you-xian-bian-li-dfs-or-/
# 我悟了
# 如果是原地修改矩阵，则在递归内部传参；
# 如果是visited数组，则需要在递归外部就传；
"""
# 思路
# 目标是找到矩阵中 “岛屿的数量” ，上下左右相连的 1 都被认为是连续岛屿。
# dfs方法： 设目前指针指向一个岛屿中的某一点 (i, j)，寻找包括此点的岛屿边界。
# 从 (i, j) 向此点的上下左右 (i+1,j),(i-1,j),(i,j+1),(i,j-1) 做深度搜索。
# 终止条件：
    # (i, j) 越过矩阵边界;
    # grid[i][j] == 0，代表此分支已越过岛屿边界。
# 搜索岛屿的同时，执行 grid[i][j] = '0'，即将岛屿所有节点删除，以免之后重复搜索相同岛屿。
# 主循环：
    # 遍历整个矩阵，当遇到 grid[i][j] == '1' 时，从此点开始做深度优先搜索 dfs，岛屿数 count + 1 且在深度优先搜索中删除此岛屿。
    # 最终返回岛屿数 count 即可。
class Solution:
    # bfs解法
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        res = 0
        queue = []
        m, n = len(grid), len(grid[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        # print(m,n)
        for i in range(m):
            for j in range(n):
                # 只要是陆地，且没有被访问过的，就可以使用 BFS 发现与之相连的陆地，并进行标记
                if not marked[i][j] and grid[i][j]=='1':
                    res+=1
                    queue.append((i,j))
                    marked[i][j] = True # 标记访问过的节点
                    while queue:
                        a,b = queue.pop(0)
                        dx = [-1,0,1,0]
                        dy = [0,1,0,-1]
                        for z in range(4):
                            x = a+dx[z]
                            y = b+dy[z]
                            # 如果不越界、没有被访问过、并且还要是陆地，我就继续放入队列，放入队列的同时，要记得标记已经访问过
                            if m>x>=0 and n>y>=0 and not marked[x][y] and grid[x][y]=='1':
                                queue.append((x,y))
                                marked[x][y] = True
        return res

    # dfs解法
    def numIslands_dfs(self, grid):
        if not grid or not grid[0]:
            return 0
        count = 0 # 计数岛屿数量
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j)
        return count


    def dfs(self, grid, x, y):
        m, n = len(grid), len(grid[0])
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]

        grid[x][y] = '0' # 将访问过的1都换为0
        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if a>=0 and a<m and b>=0 and b<n and grid[a][b]=='1':
                self.dfs(grid, a, b)

        return

if __name__ == '__main__':
    # grid = [['1', '1', '1', '1', '0'],
    #         ['1', '1', '0', '1', '0'],
    #         ['1', '1', '0', '0', '0'],
    #         ['0', '0', '0', '0', '1']] #2
    grid = [["1", "0"]] # 1
    # print(Solution().numIslands(grid))
    print(Solution().numIslands_dfs(grid))