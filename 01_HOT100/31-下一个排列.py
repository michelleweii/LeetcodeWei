"""
middle 2022-03-03 双指针
题目：是指其整数的下一个字典序更大的排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列。
必须 原地 修改，只允许使用额外常数空间
从后向前遍历，找到一个后半段最小的数，index=i
再从后向前遍历，找到一个比index=i刚刚大一点点数，进行交换，index=k
j=i+1, 对[j,k]重置为升序。
"""
# 2022-04-18 总结
# 找一个较小的数（前），找一个比较小数稍微大一点的数（后），两者交换，
# （后半段）小数后面，升序排序
"""
该题本质：字典序排序
middle 2021-06-08 从后向前遍历双指针(严格来说不算双指针) （字节、虾皮）
1、在尽可能靠右的低位进行交换，需要从后向前查找
2、将一个 尽可能小的「大数」 与前面的「小数」交换。
比如 123465，下一个排列应该把 5 和 4 交换而不是把 6 和 4 交换
3、将「大数」换到前面后，需要将「大数」后面的所有数重置为升序，升序排列就是最小的排列。
以 123465 为例：首先按照上一步，交换 5 和 4，得到 123564；
然后需要将 5 之后的数重置为升序，得到 123546。
显然 123546 比 123564 更小，123546 就是 123465 的下一个排列。

链接：https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-suan-fa-xiang-jie-si-lu-tui-dao-/
"""
class Solution:
    def nextPermutation(self, nums):
        if len(nums)<1:return nums
        # i是小数、k是大数
        i,j,k = len(nums)-2, len(nums)-1, len(nums)-1
        # 找到i,j // find: A[i]<A[j]
        while i>=0 and nums[i]>=nums[j]:
            i -= 1
            j -= 1
        # 寻找k，大数【这一步老忘】[2,3,1]->[3,1,2]
        if i >= 0: # 不是最后一个排列
            # // find: A[i] < A[k]
            while nums[i]>=nums[k]:
                k-=1 # j后的数必然降序，现在需要找到比nums[i]大的数
            # // swap A[i], A[k]
            nums[i],nums[k] = nums[k],nums[i]
        # // reverse A[j:end]
        # 将j后面的数字升序
        # 切片操作不是原地操作，所以nums[i+1:].sort()并不是对原数组排序
        # print(i,j)
        nums[j:] = sorted(nums[j:])
        # return nums
if __name__ == '__main__':
    # nums = [1, 2, 3] # 132 # 算法需要将给定数字序列重新排列成字典序中下一个更大的排列（即，组合出下一个更大的整数）
    nums = [3,2,1]  # [1,2,3] # 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）
    print(Solution().nextPermutation(nums))
