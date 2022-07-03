def fn(n, m, matrix):
    visited = [[False for i in range(m)] for j in range(n)]
    res = []
    for i in range(n):
        tmp = []
        for j in range(m):
            tmp.append(dfs(matrix, i, j, visited))
        res.append(tmp[:])
    return res


def dfs(matrix, x, y, visited):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0
    if matrix[x][y] == 0: return 0
    # tmp = matrix[x][y]
    visited[x][y] = True
    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]
        if a >= 0 and a < n and b >= 0 and b < m and not visited[a][b]:
            cnt += dfs(matrix, a, b, visited)
    # matrix[x][y]= tmp
    visited[x][y] = False
    cnt += 1
    return cnt


if __name__ == '__main__':
    # s = input().strip().split('')
    # n = int(s[0])
    # m = int(s[1])
    # matrix = []
    # while n:
    #    tmp = input().strip()
    #    tmp = [int(x) for x in tmp]
    #    matrix.append(tmp)
    #    n-=1
    n, m = 3, 3
    matrix = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
    res = fn(n, m, matrix)
    for i in range(n):
        tmp = [str(x) for x in res[i]]
        print(" ".join(tmp))


# 我的做法返回的是
# 4 4 4
# 0 4 0
# 0 0 0
# 不能找到最小的

"""
给定一个由0、1数字组成的矩阵，输出同大小的矩阵，输出矩阵的每一个元素是原矩阵对应元素离数字0的最近距离。

输入描述
输入矩阵行数r，列数c，以及0,1数字组成的矩阵
输出描述
与输入矩阵相同维度的矩阵
示例1
输入
3 3
1 1 1
0 1 0
0 0 0

输出
1 2 1
0 1 0
0 0 0
"""