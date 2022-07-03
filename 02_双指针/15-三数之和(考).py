"""
middle 2021-12-30 同向双指针
2020年平安科技实习生面试过此题，当时给的方案是哈希表，现在想想面试官应该想考察的是双指针
题目要求，a+b+c=0
https://leetcode-cn.com/problems/3sum/solution/pai-xu-shuang-zhi-zhen-zhu-xing-jie-shi-python3-by/
"""
# 3个指针，一个指向cur,一个cur+1,一个lens-1。（每固定一个a，就在右区间找相应的b+c [left,right]）
# 时间复杂度：O(n^2)
# 本题的难点在于如何去除重复解。
class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        res = []
        # 特例
        if (not nums or n < 3):
            return res
        # 对nums升序 nlogn
        nums.sort()
        for i in range(n):
            # 遍历每个元素，以每个元素为原点开始向右区间计算
            if nums[i]>0:return res # 因为升序，所以后面不可能有三个数加和等于0，直接返回结果。
            # 剪枝，当前元素已经遍历过
            if i>0 and nums[i]==nums[i-1]:continue # 本题的难点在于如何去除重复解。## 这种方式回溯里也会用到
            left = i+1
            right = n-1
            while left<right:
                cur_res = nums[i] + nums[left] + nums[right]
                if cur_res == 0:
                    res.append([nums[i],nums[left],nums[right]])
                    # 判断左界和右界是否和下一位置重复，去除重复解。(本题重点) ### 本题的难点在于如何去除重复解。
                    # 并同时将 L,R 移到下一位置，寻找新的解
                    while left<right and nums[left]==nums[left+1]:left+=1
                    while left<right and nums[right]==nums[right-1]:right-=1
                    left += 1 # 不要忘了，否则不能退出while循环
                    right -= 1
                elif cur_res>0: # 右边right太大了，right--
                    right-=1
                else: # 左边left太小了，left++
                    left+=1
        return res

if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    print(Solution().threeSum(nums))
    # [[-1, -1, 2], [-1, 0, 1]]