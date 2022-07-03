"""
easy 反向双指针
2021-07-22
"""

class Solution:
    def exchange(self, nums):
        n = len(nums)
        i, j = 0, n-1
        while i<j:
            if i<n and nums[i]%2==1: i+=1
            if j>=0 and nums[j]%2==0: j-=1
            else: nums[i], nums[j] = nums[j], nums[i]
        return nums



if __name__ == '__main__':
    nums = [1,2,3,4]
    print(Solution().exchange(nums))