"""
2021-12-14 前缀和+哈希表
先对原数组求个前缀和
求前缀和技巧：sum表示前缀和，i-j前缀的和为nums[i...j]=sum[j]-sum[i-1]
https://leetcode-cn.com/problems/subarray-sum-equals-k/solution/dai-ni-da-tong-qian-zhui-he-cong-zui-ben-fang-fa-y/
思路：
这道题即“求前缀和=2的数量”
1、先求出nums的前缀和sums；
2、求满足`prefixSum[j] - prefixSum[i - 1] == k`的个数；
"""
class Solution:
    # 简单前缀和，时间复杂度O(N^2)
    # 有几种 i、j 的组合，满足 prefixSum[j] - prefixSum[i - 1] == k
    def subarrySum_native(self, nums, k):
        n = len(nums)
        # 计算前缀和数组
        pre_sum = [0]*(n+1)
        for i in range(n):
            pre_sum[i+1] = pre_sum[i]+nums[i]
        # print(pre_sum) # [0, 1, 2, 3]
        count = 0
        for left in range(0, n):
            for right in range(left, n):
                # 区间和 [left..right]，注意下标偏移
                # 求前缀和=2的数量
                if pre_sum[right+1]-pre_sum[left]==k: # 【Attention】
                    count += 1
        return count

    # 前缀和 + 哈希表优化，时间复杂度O(N)
    # key: 前缀和
    # value: key 对应的前缀和的个数
    def subarraySum(self, nums, k):
        hash_map = {}
        hash_map[0] = 1 # 前缀和为0的数量有1个。默认nums[-1]=0
        res = 0
        sums = 0 # 前缀和
        for x in nums:
            sums += x
            # print(sums) # 1,2,3
            # 问自己！当前前缀和（sums）-k，之前出现过吗？如果出现过了记作a，那么sums-a=k，count++
            # (a,b)=presum[b]-presum[a]=k
            # presum[b]=sums
            # 求a出现过几次
            res += hash_map.get(sums-k, 0) # hash_map[sums-k] KeyError: -1
            # 维护hashmap的定义
            hash_map[sums] = hash_map.get(sums, 0) + 1 # 计算前缀和为sums的个数

        # print(hash_map) # {0: 1, 1: 1, 2: 1, 3: 1}
        return res
    """
    不用求出 prefixSum 数组
    其实我们不关心具体是哪两项的前缀和之差等于k，只关心等于 k 的前缀和之差出现的次数c，就知道了有c个子数组求和等于k。
    遍历 nums 之前，我们让 -1 对应的前缀和为 0，这样通式在边界情况也成立。即在遍历之前，map 初始放入 {0:1} 键值对（前缀和为0出现1次了）。
    遍历 nums 数组，求每一项的前缀和，统计对应的出现次数，以键值对存入 map。`hash_map[sums] = hash_map.get(sums, 0) + 1 `
*    边存边查看 map，如果 map 中存在 key 为「当前前缀和 - k」，说明这个之前出现的前缀和，满足「当前前缀和a - 该前缀和b == k」，它出现的次数，累加给 count。
*   「当前前缀和 - 该前缀和 == k」等价于 「该前缀和 == 当前前缀和-k」

    遍历数组，根据当前“前缀和”，在 map 中寻找「与之相减 == k」的历史前缀和
    当前“前缀和”与历史前缀和，差分出一个子数组，该历史前缀和出现过 c 次，就表示当前项找到 c 个子数组求和等于 k。
    遍历过程中，c 不断加给 count，最后返回 count。
    """

if __name__ == '__main__':
    nums = [1, 1, 1]
    k = 2
    # print(Solution().subarrySum_native(nums, k))
    print(Solution().subarraySum(nums, k))

#
# nums = [1,2,5,9]
# n = len(nums)
# for i in range(n):
#     for j in range(i):
#         # print("idx----------------------",i,j)
#         # print("val",nums[i], nums[j])
#         print(i,j)
#
# print('-'*10)
#
# for k in range(n):
#     for m in range(k+1,n):
#         print(k,m)
#