"""
middle 3_bfs-队列
所有可行解
"""
class Solution:
    def get_sum(self, n):
        s = 0
        while n:
            s += n%10
            n //= 10
        return s

    def movingCount(self, m, n, k):
        if not m and not n: return 0
        res = 0
        visited = [[False for _ in range(n)] for _ in range(m)]
        queue = []
        queue.append((0, 0))
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        while queue:
            tmp = queue.pop(0)
            if self.get_sum(tmp[0])+self.get_sum(tmp[1])>k or visited[tmp[0]][tmp[1]]:continue
            res += 1
            visited[tmp[0]][tmp[1]] = True
            for i in range(4):
                a = tmp[0]+dx[i]
                b = tmp[1]+dy[i]
                if a>=0 and a<m and b>=0 and b<n and not visited[a][b]:
                    queue.append((a,b))
        return res

if __name__ == '__main__':
    # m = 2
    # n = 3
    # k = 1
    m = 3
    n = 1
    k = 0
    # print(Solution().get_sum(11))
    print(Solution().movingCount(m,n,k))
