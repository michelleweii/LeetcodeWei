# -*- coding:utf-8 -*-
from collections import deque
# 主要思想是：
# 每次比末尾元素大的才可以入队列
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        res = []
        if not size or not num: return res
        # 可在两端进行插入和删除
        q = deque()
        # 队列存在的是下标，不是数值
        for i in range(len(num)):
            # 如果超出滑动窗口，那么把队首元素踢掉，双端队列是不排序的
            while q and q[0] <= i-size:
                q.popleft()
            # 优胜劣汰，弱的出去，强的进来
            # 如果当前元素大于队尾元素，入队
            while q and num[i] >= num[q[-1]]:
                q.pop()
            q.append(i)
            # 返回结果
            if i >= size-1:
                res.append(num[q[0]])
        return res

if __name__ == '__main__':
    num = 2,3,4,2,6,2,5,1
    size = 3
    print(Solution().maxInWindows(num,size))