"""
middle 2022-05-05 前缀和（pdd面筋）
【看图】https://leetcode-cn.com/problems/continuous-subarray-sum/solution/523-lian-xu-de-zi-shu-zu-he-qian-zhui-he-zl78/
# 同余定理：即当两个数除以某个数的余数相等，那么二者相减后肯定可以被该数整除。
# 哈希表记录{余数 : 下标}，由于可能存在nums前N个数字和恰好被K整除的情况，我们预制字典{0,-1}来规避该问题。
# 看到几项的和为条件判断，那么首先改考虑前缀和了。nums[i-j]=presum[j]-presum[i-1]
"""
# 需要满足条件
# 子数组大小 至少为 2
# 子数组元素总和为 k 的倍数

class Solution:
    def checkSubarraySum(self, nums, k): #List[int], k: int) -> bool:
        hashmap = {0:-1}
        presum=0
        for i in range(len((nums))):
            presum+=nums[i]
            rem=presum%k
            pre_i = hashmap.get(rem, i)
            if pre_i==i: # 存在两个数，他们的余数相同
                hashmap[rem]=i # 更新成最新的下标
            elif i-2>=pre_i:
                return True
        return False

if __name__ == '__main__':
    nums = [23, 2, 4, 6, 7]
    k = 6
    # [2,4] 是一个大小为 2 的子数组，并且和为 6
    print(Solution().checkSubarraySum(nums,k))