# -*- coding:utf-8 -*-
# 糖果
import math
# 自己建图，再广搜
def Solution(N):
    nums = [int(x) for x in input().split()]
    M = []
    for i in range(N):
        tmp = [0] * N
        M.append(tmp)

    for i in range(N):
        for j in range(i, N):
            if math.gcd(nums[i], nums[j]) > 1:
                M[i][j], M[j][i] = 1, 1

    flag = [False] * N
    q = []
    res = 0
    maxres = 0

    for start in range(N):
        if not flag[start]:
            if res > maxres:
                maxres = res
            res = 0
            q.append([start])
            while q:
                nowq = q.pop(0)
                tmp = []
                while nowq:
                    res += 1
                    now = nowq.pop(0)
                    flag[now] = True
                    for i in range(N):
                        if M[now][i] > 0 and not flag[i]:
                            tmp.append(i)
                            flag[i] = True
                if tmp:
                    q.append(tmp)
    return maxres


# tmp = input()
N = int(input())

res = Solution(N)
print(res)