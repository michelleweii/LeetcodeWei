def hasPath(matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        if not rows:return
        visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(rows):
            for j in range(cols):
                if dfs(matrix,i,j,0,visited):
                    return True
        return False

def dfs(matrix,a,b,cnt,visited):
        if :cnt+=1
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        for i in range(4):
            visited[a][b] = True
            x = a+dx[i]
            y = b+dy[i]
            if x>=0 and x<len(matrix) and y>=0 and y<len(matrix[0]) and not visited[x][y]:
                if dfs(matrix,x,y,cnt,visited):return True
        visited[a][b] = False
        return False

if __name__ == '__main__':
    matrix = [[3,1,2,1,1],[1,1,1,1,3],[1,1,1,1,1],[1,1,1,1,1],[3,1,2,2,2]]
    print(hasPath(matrix))

# if __name__ == '__main__':
#     n = input().strip()
#     n = int(n)
#     q = input().strip().split()
#     nums = [int(i) for i in q]
#
#     # n = 4
#     # nums = [1,2,3,1]
#     res = fn1()
#     print(res)