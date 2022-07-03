# -*- coding:utf-8 -*-
# 宽度优先遍历
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        cnt = 0
        if not rows or not cols:return cnt
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        # print(visited)
        queue = []
        queue.append([0,0]) # 从起点开始
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        while queue:
            tmp = queue[0]
            # print(tmp)
            queue.pop(0)
            if self.get_sum(tmp)>threshold or visited[tmp[0]][tmp[1]]:continue
            cnt += 1
            visited[tmp[0]][tmp[1]] = True
            for i in range(4):
                x = tmp[0]+dx[i]
                y = tmp[1]+dy[i]
                if x>=0 and x<rows and y>=0 and y<cols:
                    queue.append([x,y])
        return cnt

    def get_single_sum(self,x):
        s = 0
        while x:
            s += x%10
            x //= 10
        return s

    def get_sum(self,pair):
        return self.get_single_sum(pair[0])+ \
               self.get_single_sum(pair[1])

if __name__ == '__main__':
    threshold = 7
    rows = 4
    cols = 5
    # print(Solution().get_single_sum(12))
    print(Solution().movingCount(threshold,rows,cols))