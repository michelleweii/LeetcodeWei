"""
easy 2021-09-07 同向双指针<--因为要保证顺序不变。
要求：不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
因为数组是有序的，那么重复的元素一定会相邻。
"""
# 如果两个元素相等，j++
# 不相等，i++, nums[i]=nums[j]
class Solution:
    def removeDuplicates(self, nums):
        # i 左边是已经处理好的元素；
        # 元素如果要话，ij都要右移；
        # 元素如果不要的话，j右移，i不动；
        # 当ij不在同一个位置上时，j标记的位置如果要的话，则将j的值赋给i。i++
        # 【i 左边是处理好的元素】。
        i, j = 0, 1
        # i=0说明i左边什么都没有，第一个元素肯定是不重复的
        while j < len(nums):
            # 如果相等，j++
            if nums[i]==nums[j]:
                j+=1
            else:
                i+=1
                nums[i]=nums[j] # 是赋值操作，不是交换操作！
            # print(i, j, nums)
            # 0 2 [1, 1, 2]
            # 1 2 [1, 2, 2]
            # 1 3 [1, 2, 2]
        return i+1 # 2

if __name__ == '__main__':
    nums = [1, 1, 2]
    print(Solution().removeDuplicates(nums))