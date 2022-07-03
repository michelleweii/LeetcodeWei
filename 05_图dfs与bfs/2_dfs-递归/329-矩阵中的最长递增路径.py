"""
hard 2022-05-22 记忆化dfs
https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/solution/ju-zhen-zhong-de-zui-chang-di-zeng-lu-jing-by-le-2/
https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/solution/tong-ge-lai-shua-ti-la-yi-ti-si-jie-bfs-agawl/
问题转化成『在有向图中寻找最长路径』
没有记忆搜索会超出时间范围
"""
class Solution:
    def longestIncreasingPath(self, matrix): #List[List[int]]) -> int:
        if not matrix:return 0
        max_path=0
        m,n=len(matrix),len(matrix[0])
        # 记忆化搜索
        # 由于同一个单元格对应的最长递增路径的长度是固定不变的，因此可以使用记忆化的方法进行优化。
        # 用矩阵 memo 作为缓存矩阵，已经计算过的单元格的结果存储到缓存矩阵中。
        memo=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # 记忆化搜索
                # 说明该单元格的结果已经计算过memo[i][j]=1，则直接从缓存中读取结果，
                # memo[i][j]=0，说明该单元格的结果尚未被计算过，则进行搜索，并将计算得到的结果存入缓存中。
                if memo[i][j]==0:
                    path=self.dfs(matrix,i,j,memo)
                    max_path=max(max_path,path)
        return max_path

    def dfs(self,mat,x,y,memo):
        # 从该单元格(x,y)开始的最长递增路径
        if memo[x][y]!=0:return memo[x][y] # 已经遍历过，直接返回
        path=1
        dx=[-1,0,1,0]
        dy=[0,1,0,-1]
        for i in range(4):
            a=x+dx[i]
            b=y+dy[i]
            if a>=0 and a<len(mat) and b>=0 and b<len(mat[0]) and \
                mat[a][b]>mat[x][y]: # 符合递增
                tmp=self.dfs(mat,a,b,memo)
                path=max(path,tmp+1)
        # 记录到缓存中
        memo[x][y]=path
        return path

if __name__ == '__main__':
    # 输入：matrix = [[9,9,4],[6,6,8],[2,1,1]]
    # 输出：4
    # 解释：最长递增路径为 [1, 2, 6, 9]。
    mat=[[9,9,4],[6,6,8],[2,1,1]]
    print(Solution().longestIncreasingPath(mat))