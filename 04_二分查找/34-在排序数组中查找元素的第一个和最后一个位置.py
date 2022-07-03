"""
middle 2022-03-02 二分查找
【同一个模板】https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/tu-jie-er-fen-zui-qing-xi-yi-dong-de-jia-ddvc/
思路：左边一次二分、右边一次二分
2022-03-02 AC
"""
class Solution(object):
    def searchRange(self, nums, target):
        if not nums:return [-1,-1]
        res = []
        # 二分左边界
        l,r=0,len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]<target:
                l=mid+1
            else:
                r=mid
        # print(r, nums[r])
        if nums[r]!=target:return [-1,-1]
        res.append(r)

        # 二分右边界
        l,r=0,len(nums)-1
        while l<r:
            mid = (l+r+1)//2
            if nums[mid]>target:
                r=mid-1
            else:
                l=mid
        # print(l, nums[l])
        # if nums[l]!=target:return [-1,-1]
        res.append(l)
        return res

if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(Solution().searchRange(nums,target))


