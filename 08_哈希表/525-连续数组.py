"""
middle
哈希表
560: 记录总共有几个序列 hash记录前缀和出现多少次
525: 求最长子段的长度 hash记录前缀和的下标,记录最早出现的位置
将所有0都变为-1，然后求和等于0的个数
思路：
# 从0到i-1里，前缀和有没有一个等于当前前缀和的相反数，如果有的话，
# 找一下离的最远的前缀和在哪，所以记录的是下标。
# 枚举，找到一个等于当前前缀和的相反数，if有，找最远的前缀和在哪
k:到i为止的前缀和
v:index只记录最早出现的下标
"""
class Solution:
    def findMaxLength(self, nums):
        hash_map = {}
        hash_map[0] = -1  # sum[-1]=0
        s = 0 # 从0-i的前缀和
        res = 0
        for i in range(len(nums)):
            # 到i为止的前缀和s
            s = s + (nums[i] if nums[i]==1 else -1)
            # if hash_map.get(s,0):  # 这样会丢掉{-1: 0} 这样的情况
            if s in hash_map: # s-s=0
                # 如果当前前缀和在之前已经存过
                res = max(res, i-hash_map[s])
            else:
                hash_map[s] = i # 只记录最远的下标，所以该前缀和从来没有出现过才记录
        return res


if __name__ == '__main__':
    # nums =  [0,1,0]
    nums = [0,0,1]
    res = Solution()
    print(res.findMaxLength(nums))