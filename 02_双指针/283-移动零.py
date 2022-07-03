"""
easy 2021-09-09 同向双指针
https://leetcode-cn.com/problems/move-zeroes/solution/dong-hua-yan-shi-283yi-dong-ling-by-wang_ni_ma/
# 移动非零元素（操作次数就是非零元素的个数）
# j 记录非零元素应该换到第几个位置，记录0的位置
# i 遍历数组
"""
class Solution:
    def moveZeroes(self, nums):
        slow, fast = 0, 0 # fast从1开始就是无序状态，0开始就是有序状态
        while fast<len(nums):
            if nums[fast]!=0:
                nums[slow],nums[fast]=nums[fast],nums[slow]
                slow += 1
            fast+=1
        return nums
        # j = 0
        # for i in range(len(nums)):
        #     if nums[i] !=0:
        #         # print(i, j)
        #         nums[i],nums[j] = nums[j],nums[i]
        #         j+=1
        #
        # return nums


if __name__ == '__main__':
    nums = [1,1,0,3,12] # [1, 1, 3, 12, 0]
    myResult = Solution()
    print(myResult.moveZeroes(nums))