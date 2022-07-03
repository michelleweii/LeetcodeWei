"""
easy 2022-03-02 二分查找【基础二分模板】
https://leetcode-cn.com/problems/search-insert-position/solution/te-bie-hao-yong-de-er-fen-cha-fa-fa-mo-ban-python-/
2022-03-02 AC
"""
class Solution(object):
    def searchInsert(self, nums, target):
        if not nums:return 0
        l,r=0,len(nums)
        while l<r:
            mid=(l+r)//2
            if nums[mid]<target:
                l = mid+1
            else:
                r=mid
        # print(r, nums[r])
        return r

if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 5
    print(Solution().searchInsert(nums, target))