def Solution(N):
# 油豆瓶
#     M = []
#     for i in range(N):
#         input_x = [int(x) for x in input().split()]
#         M.append(input_x)
    M = [[0,4,0], [4,0,0], [0,0,0]]
    flag = [False] * N
    q = []
    res = 0
    for start in range(N):
        if not flag[start]:
            res += 1
            q.append(start)
            while q:
                now = q.pop(0)
                print("now",now)
                flag[now] = True
                for i in range(N):
                    if M[now][i] >= 3 and not flag[i]:
                        q.append(i)
                        flag[i] = True

    return res

# tmp = input()
# N = int(input())
N = 3
res = Solution(N)
print(res)
# def fn1(n,array):
#     if not array:return 0
#     for i in range(n):
#         for j in range(n):
#
#
#
# if __name__ == '__main__':
#     N = input().strip()
#     N = int(N)
#     mat = []
#     while N:
#         tmp = input().strip().split(" ")
#         tmp = [int(ch) for ch in tmp]
#         mat.append(tmp)
#         N-=1
#     fn1(N,mat)
