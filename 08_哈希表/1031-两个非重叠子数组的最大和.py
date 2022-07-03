"""
middle 2022-05-20 前缀和
求区间和，直接整一个前缀和数组prefix_sum出来!!!
https://leetcode.cn/problems/maximum-sum-of-two-non-overlapping-subarrays/solution/qian-zhui-he-by-a-zhu-8o-9w2a/
情况1，L在M左侧，可以考虑从左往右依次枚举M的起始点
M的起始点每向右移动一格，L可以取的区间也右移一格，如果新的L区间，元素和更大，那么更新L的最大元素和。
情况2，M在L左侧，过程同上，依葫芦画瓢重复一次即可。
"""
class Solution:
    def maxSumTwoNoOverlap(self, nums, firstLen: int, secondLen: int): #-> int:
        n=len(nums)
        # 闭区间[i, j]的区间和 = prefix_sum[j+1] – prefix_sum[i]
        # nums=[0, 6, 5, 2, 2, 5, 1, 9, 4]
        presum=[0]*(n+1)
        for i in range(len(nums)):
            presum[i+1]=presum[i]+nums[i]
        # print(presum) # [0, 0, 6, 11, 13, 15, 20, 21, 30, 34]

        # L在M左侧，
        # i 枚举M的起始点
        res1,tmp=0,0 # temp记录L的最大元素和
        for i in range(firstLen,n-secondLen+1):
            # temp记录L的最大元素和
            tmp=max(tmp, presum[i]-presum[i-firstLen]) # [i-L]~[i-1]的区间值
            # res1记录L+M的最大和
            res1=max(res1,tmp+presum[i+secondLen]-presum[i]) # [i]~[i+M-1]

        # M在L左侧，
        # i枚举L的起始点
        res2,tmp=0,0 # temp记录M的最大元素和
        for i in range(secondLen, n-firstLen+1):
            tmp=max(tmp,presum[i]-presum[i-secondLen])
            res2=max(res2,tmp+presum[i+firstLen]-presum[i])
        return max(res1,res2)

if __name__ == '__main__':
    A = [0, 6, 5, 2, 2, 5, 1, 9, 4]
    L = 1
    M = 2
    print(Solution().maxSumTwoNoOverlap(A,L,M)) # 20 子数组的一种选择中，[9] 长度为 1，[6,5] 长度为 2。