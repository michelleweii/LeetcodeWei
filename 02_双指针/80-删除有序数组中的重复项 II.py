"""
middle 2021-06-16 快慢指针
# 27,26，283 思路相同
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/solution/gong-shui-san-xie-guan-yu-shan-chu-you-x-glnq/
解法一：
- 由于是保留 k 个相同数字，对于前 k 个数字，我们可以直接保留
- 对于后面的任意数字，能够保留的前提是：与当前写入的位置前面的第 k 个元素进行比较，不相同则保留

解法二：快慢指针
"""
class Solution:
    # 通解
    def removeDuplicates(self, nums):
        return self.process(nums, 2) # 函数应返回新长度
    def process(self, nums, k):
        u = 0
        for x in nums:
            if u < k or nums[u - k] != x:
                nums[u] = x
                u += 1
        # print(nums, u) # [1, 1, 2, 2, 3, 3] 5
        return u

    # 快慢指针 类似LC27
    def two_pointers(self, nums):
        n = len(nums)
        if n<=2:return n
        slow, fast = 1, 2 # 初始值的设定依据题意
        while fast<n:
            # 相同则跳过，不相同则覆盖
            if nums[slow-1]!=nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        print(nums)
        return slow+1 # 一定要是slow+1


if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    print(Solution().removeDuplicates(nums))
    print(Solution().two_pointers(nums))