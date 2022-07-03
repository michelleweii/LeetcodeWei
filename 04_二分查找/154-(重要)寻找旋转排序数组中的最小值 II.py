"""
hard 2021-12-08 二分
https://leetcode-cn.com/problems/search-in-rotated-sorted-array/solution/leetcode-33-sou-suo-xuan-zhuan-pai-xu-sh-ga4b/
有序数组的排序——二分（可能存在【重复】元素值的数组 nums）
基础题153（元素值【互不相同】的数组 nums）
"""
class Solution:
    def findMin(self, nums): #: List[int]) -> int:
        n = len(nums)-1
        # 恢复两段性
        while (n>0 and nums[0]==nums[n]):n-=1 # 存在重复元素值的关键步骤
        if nums[0]<nums[n]:return nums[0] # 递增序列
        l, r = 0, n
        # 假设mid在左边，区间被划分为[left,mid] [mid+1,right]
        # mid在左边，意味着res在右边
        while l<r:
            mid = (l+r)//2
            # 这个好难理解啊
            # if nums[mid]<nums[0]:r=mid
            # else:l=mid+1
            if nums[mid]>=nums[0]:l=mid+1
            else:r=mid
        return nums[l]

if __name__ == '__main__':
    nums = [2,2,2,0,1,2]
    print(Solution().findMin(nums))