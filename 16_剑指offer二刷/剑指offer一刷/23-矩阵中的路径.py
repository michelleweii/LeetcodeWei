# -*- coding:utf-8 -*-
# leetcode79:单词搜索
# newcoder上就是不通过
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(rows):
            # print()
            for j in range(cols):
                if self.dfs(matrix,path,i,j,0,visited):
                    # print("bbb")
                    return True
        return False

    def dfs(self,matrix,path,a,b,u,visited):
        # print("path",len(path))
        # print("u",u)
        # print("m:",matrix[a][b])
        # print("path",path[u])
        # print(matrix[a][b] == path[u])
        if matrix[a][b] != path[u]: return False
        if len(path) == u+1:return True
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        for i in range(4):
            visited[a][b] = True
            x = a+dx[i]
            y = b+dy[i]
            if x>=0 and x<len(matrix) and y>=0 and y<len(matrix[0]) and not visited[x][y]:
                # print("yes")
                if self.dfs(matrix,path,x,y,u+1,visited):return True
        # print("q")
        visited[a][b] = False
        # print("a")
        return False

if __name__ == '__main__':
    matrix = [["a","b","c","e"],
              ['s','f','c','s'],
              ['a','d','e','e']]
    matrix = [["a"]]
    matrix = [["A",'B','C',"E"],
              ["S",'F','C',"S"],
              ["A",'D','E',"E"]]
    # print(matrix[2][3])
    # matrix[2][3] = "@"
    # print(matrix)
    # lucky = "abc"
    # lucky[1]="!"
    # print(lucky)
    # lucky[1]="!"
    # TypeError: 'str' object does not support item assignment
    row = 1
    col = 1
    row=3
    col=4
    path = "bcced"
    path = "abcb"
    path = "b"
    path = "ABCCED"
    print(Solution().hasPath(matrix,row,col,path))