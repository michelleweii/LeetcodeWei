"""
easy 数学题/二分
2021-07-18
https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/solution/mian-shi-ti-53-ii-0n-1zhong-que-shi-de-shu-zi-er-f/
"""
class Solution:
    def missingNumber1(self, nums):
        n = len(nums)+1
        s = (0+n)*(n-1)//2
        for x in nums:
            s -= x
        return s

    def missingNumber(self, nums):
        l,r = 0,len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]==mid:l=mid+1
            else:r=mid
        return l


if __name__ == '__main__':
    nums = [0,1,2,3,4,5,6,7,9]
    print(Solution().missingNumber(nums))