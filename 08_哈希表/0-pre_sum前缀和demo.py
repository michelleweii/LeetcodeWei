"""
前缀和
560.和为K的子数组
"""
# 闭区间[i, j]的区间和 = prefix_sum[j+1] – prefix_sum[i]
nums=[0, 6, 5, 2, 2, 5, 1, 9, 4]
presum = [0] * (len(nums)+1)
for i in range(len(nums)):
    presum[i+1] = presum[i] + nums[i]
# print(presum) # [0, 0, 6, 11, 13, 15, 20, 21, 30, 34]


# n = 3
# for i in range(0, n):
#     for j in range(0, i):
#         print(i, j)
# # 1 0
# # 2 0
# # 2 1
# print('*'*10)
#
# for i in range(0, n):
#     for j in range(i, n):
#         print(i, j)
# # 0 0
# # 0 1
# # 0 2
# # 1 1
# # 1 2
# # 2 2

if __name__ == '__main__':
    nums, k = [1,1,1], 2
    hash_map = {}
    hash_map[0] = 1 # 前缀和为0的数量有1个。默认nums[-1]=0
    res = 0
    sums = 0 # 前缀和
    for x in nums:
        sums += x
        res += hash_map.get(sums-k, 0) # hash_map[sums-k] KeyError: -1
        hash_map[sums] = hash_map.get(sums, 0) + 1

    print(hash_map) # {0: 1, 1: 1, 2: 1, 3: 1}

    print('res', res)
