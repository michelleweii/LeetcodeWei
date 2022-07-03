
# 2022-03-01
class solution(object):
    def search(self, nums, target):
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
                l,r=0,r
            else:
                l,r=l,n

        #
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
    # nums = [2, 5, 6, 0, 0, 1, 2]
    # target = 0
    # nums = [1,0]#[1,0,1,1,1]
    # target = 0
    # nums=[1, 3]
    # target= 3
    nums=[3,1]
    target = 3
    print(solution().search(nums, target))
