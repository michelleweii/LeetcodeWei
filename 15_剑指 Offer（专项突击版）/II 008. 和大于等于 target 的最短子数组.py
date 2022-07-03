"""
middle 2022-05-13 双指针
https://leetcode.cn/problems/2VG8Kg/solution/shua-chuan-jian-zhi-offer-day06-shu-zu-i-d5ne/
1.如果两个指针之间的子数组中所有数字之和小于target，那么把右边界向右移动
2.滑动窗口的总体思路是先移动右边界，让窗口中的值满足题目的解，也在是说在找到可行解的情况下
3.再移动左边界，在可行解里面寻找最优解
"""
class Solution:
    def minSubArrayLen(self, target: int, nums): #List[int]) -> int:
        left = total = 0
        ret = float('inf')
        for right, num in enumerate(nums):
            total += num
            while total >= target:
                ret = min(ret, right - left + 1)
                total -= nums[left]
                left += 1
        return 0 if ret > len(nums) else ret

if __name__ == '__main__':
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(Solution().minSubArrayLen(target,nums))