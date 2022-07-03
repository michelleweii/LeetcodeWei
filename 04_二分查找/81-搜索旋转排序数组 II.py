"""
middle 2022-02-24 与LC33的区别：LC81有重复数字
https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/solution/gong-shui-san-xie-xiang-jie-wei-he-yuan-xtam4/
“两段性”：前一半都大于nums[0]，后一半都小于nums[0]
"""
class solution(object):
    def search(self, nums, target) -> bool:
        if not nums: return False
        n = len(nums)-1
        while n>0 and nums[0]==nums[n]:n-=1

        # 第一次二分找到最小值点，找到两个递增区间
        l,r=0,n
        if nums[0]>nums[n]: # 如果是旋转区间
            while l<r:
                mid=(l+r)//2
                if nums[mid] >= nums[0]: # 边界>= 还是要带入值查一下
                    l=mid+1
                else:
                    r=mid
            print("旋转数组最小值", nums[r], "，下标是", r)

            # 第二次第二分找到target
            if target>=nums[0]:
                l,r=0,r-1
            else:l,r=r,n

        # 如果直接就是递增区间，直接进行第二次二分
        while l<r:
            mid = (l+r)//2
            if nums[mid]>=target:
                r=mid
            else:l=mid+1
        if nums[r]==target:return True
        return False


if __name__ == '__main__':
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 0
    print(solution().search(nums, target))
