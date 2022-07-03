# # 二进制
# # print('*****二进制******')
# # a = "000"
# # # print(a.lstrip('0'))
# # print(bin(000))
import math
N = 6
M = []
nums = [20,50,22,74,9,63]
for i in range(N):
    tmp = [0] * N
    M.append(tmp)
    # print(M)
    # M:建图
    # [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

for i in range(N):
    for j in range(i, N):
        if math.gcd(nums[i], nums[j]) > 1:
            M[i][j], M[j][i] = 1, 1

