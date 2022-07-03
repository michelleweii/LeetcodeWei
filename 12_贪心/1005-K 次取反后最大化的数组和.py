"""
easy 2021-12-22 贪心
分析：
贪心的思路，局部最优：让绝对值大的负数变为正数，当前数值达到最大，整体最优：整个数组和达到最大。
局部最优：只找数值最小的正整数进行反转，当前数值可以达到最大（例如正整数数组{5, 3, 1}，反转1 得到-1 比 反转5得到的-5 大多了），全局最优：整个 数组和 达到最大。
"""
class Solution:
    """
    第一步：将数组按照绝对值大小从大到小排序，注意要按照绝对值的大小
    第二步：从前向后遍历，遇到负数将其变为正数，同时K--
    第三步：如果K还大于0，那么反复转变数值最小的元素，将K用完
    第四步：求和
    """
    def largestSumAfterKNegations(self, nums, k: int):
        nums = sorted(nums, key=abs, reverse=True) # 将nums按绝对值从大到小排列
        n = len(nums)
        for i in range(n):
            if k>0 and nums[i]<0:
                nums[i] *= -1
                k -= 1
            # print(nums, k)
        if k>0: # 将小的改为负数
            # print('1')
            # 可以多次选择同一个下标 i
            nums[-1] *= (-1)**k
        return sum(nums)


if __name__ == '__main__':
    # nums = [4,2,3]
    # k = 1 # 4-2+3=5
    nums = [2,-3,-1,5,-4]
    k = 2 # 13
    print(Solution().largestSumAfterKNegations(nums, k))