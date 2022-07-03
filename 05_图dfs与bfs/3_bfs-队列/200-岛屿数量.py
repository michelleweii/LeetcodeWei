"""
middle 2021-08-25 bfs遍历模板题
"""
class Solution:
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        res = 0
        queue = []
        m, n = len(grid), len(grid[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        print(m,n)
        for i in range(m):
            for j in range(n):
                # 只要是陆地，且没有被访问过的，就可以使用 BFS 发现与之相连的陆地，并进行标记
                if not marked[i][j] and grid[i][j]=='1':
                    res+=1
                    queue.append((i,j))
                    marked[i][j] = True
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



if __name__ == '__main__':
    grid = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '1']]
    # grid = [["1", "0"]]
    print(Solution().numIslands(grid))
