"""
middle 2022-02-24 二分
【模板一样，但是用的应该是旋转数组最大值】
https://leetcode-cn.com/problems/search-in-rotated-sorted-array/solution/leetcode-33-sou-suo-xuan-zhuan-pai-xu-sh-ga4b/
思路：
需要二分2次，第一次二分找到旋转点(旋转数组最大值)，该旋转点划分了两个递增区间;
定位到递增区间后，第二次二分，找到target;
"""
# 以nums[0]作为二分分割点，前一半都大于它，后一半都小于它
# nums[0]是旋转点
class Solution:
    def search(self, nums, target):
        if not nums:return -1
        n = len(nums)
        # if nums[0]<nums[n]:min_rotate = 0
        l,r = 0,n-1
        if nums[0]>nums[n-1]:
            while l<r:
                mid = (l+r)>>1
                if nums[mid]>nums[0]:l=mid+1
                else: r=mid
            print("旋转数组最小值: ", nums[r], r)

            # 找到target属于哪一段递增区间
            if target>=nums[0]:
                l = 0
                r = r-1
                # r = l = mid # while 循环出来的位置，不用变。
                # 在前一段区间内
                # r=l # 不用重复声明
            else: # target<nums[0] 在后一段递增区间里
                l = l
                r = n-1

        print('target所在区间：', l,r)
        while l<r:
            mid = (l+r+1)//2
            if nums[mid]>target:
                r=mid-1
            else: # <=
                l=mid

        # 这里return l 还是 r是有讲究的
        # 与上面nums[mid]==target属于哪个区间有关系
        # 如果nums=[1],target=1，那么return r就会错误
        if nums[l]==target:return l
        return -1


if __name__ == '__main__':
    # nums = [4, 5, 6, 7, 0, 1, 2]
    # target = 0# 4
    nums = [1,3] #[1]
    target = 3 #1
    # nums=[4,5,6,7,0,1,2]
    # target=3
    print(Solution().search(nums, target))