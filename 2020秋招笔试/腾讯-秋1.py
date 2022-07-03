# -*- coding:utf-8 -*-
import random


def Solution(N):
    # print(N)
    M = [int(x) for x in input().split()]
    M = sorted(M)

    cnt = 0
    flag = [1]
    for i in range(1, N):
        if M[i] == M[i - 1]:
            flag[cnt] += 1
        else:
            flag.append(1)
            cnt += 1

    cnt += 1
    flag = sorted(flag)
    tmp = 0
    for i in range(cnt - 1, -1, -1):
        tmp = abs(flag[i] - tmp)

    if tmp == 0:
        return True
    else:
        return False


# tmp = input()
T = int(input())

while T:
    T -= 1

    N = int(input())
    res = Solution(N)
    # tp = random.randint(1,2)

    if res:
        print("YES")
    else:
        print("NO")