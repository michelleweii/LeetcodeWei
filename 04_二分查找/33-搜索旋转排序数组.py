"""
middle 2022-02-25 两次二分
LC81的基础题
"""
class Solution(object):
    def search(self, nums, target):
        # 需找到自增区间、旋转区间
        n = len(nums)-1
        while n>=0 and nums[0]==nums[n]:n-=1
        # print(nums[:n+1])
        l, r = 0, n

        if nums[0]>nums[n]:
            # 第一次二分，寻找旋转数组最小值
            while l<r:
                mid = (l+r)//2
                if nums[mid]>=nums[0]:
                    # print('nums[mid]>nums[0]', nums[mid],nums[0])
                    l=mid+1
                else:
                    r=mid
            print("旋转数组最小值", nums[r], "下标是", r)
            if target>=nums[0]:
                l,r=0,r # l,r=0,r-1 说明-1也是对的
            else:
                l,r=l,n
        # print(l,r,nums[l:r+1])
        # 第二次二分，寻找target下标
        while l<r:
            mid=(l+r)//2
            # print('nums[mid]',nums[mid])
            if nums[mid]<target:
                l = mid+1
            else:
                r = mid
        # print("target", nums[l])
        return l if nums[l]==target else -1



if __name__ == '__main__':
    nums = [5,1,2,3,4]
    target = 1
    print(Solution().search(nums,target))
