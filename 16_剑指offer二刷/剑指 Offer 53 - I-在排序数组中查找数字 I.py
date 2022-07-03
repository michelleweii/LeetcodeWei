"""
easy 二分
hashmap 2021-07-16 once ok
二分 2021-07018 注意这里是已经有序的nums。
https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/solution/gong-shui-san-xie-liang-chong-er-fen-ton-3epx/
"""
class Solution:
    def search_hash(self, nums, target):
        if not nums:return 0
        hashmap = {}
        for x in nums:
            hashmap[x] = hashmap.get(x,0)+1
        return hashmap.get(target,0)

    def search(self, nums, target):
        if not nums:return 0
        # 二分出左边界
        l,r = 0,len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]<target:l=mid+1
            else: r = mid
        if nums[l] != target:return 0 # 重要!
        start = l

        l, r = 0, len(nums) - 1
        while l<r:
            mid = (l+r+1)//2
            if nums[mid]>target:r=mid-1
            else: l=mid
        if nums[l] != target:return 0 # 重要！
        end = l
        # print(start,end)
        return end-start+1

        


if __name__ == '__main__':
    # nums = [5, 7, 7, 8, 8, 10]
    # target = 10
    nums = [1]
    target = 0
    # nums = [5, 7, 7, 8, 8, 10]
    # target = 6
    print(Solution().search(nums, target))