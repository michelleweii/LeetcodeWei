"""
middle 2021-09-09 同向双指针(字节、小红书、微软)
与LC3类比（没有想到的点，竟然nums不递增也可以这样做）
https://leetcode-cn.com/problems/minimum-size-subarray-sum/solution/chang-du-zui-xiao-de-zi-shu-zu-tu-jie-sh-ae80/
思路：滑动窗口区间内的值小于target,则继续扩大右边界；
区间内的值大于target,则继续移动左指针，来缩小窗口；只要一小于target就移动右指针；
需要维护min(res)，求得长度最小的子数组
1.思路很简单：count为左窗口的边界，i为右窗口的边界，多了count++，少了i++。
2.一直遍历到数组边界，不停判断即可得出答案。
"""
# 2022-01-04
class Solution:
    def myans(self, target, nums): # 套用总结模板
        # 给定一个含有 n 个正整数的数组和一个正整数 target 。
        # 找出该数组中满足其和 ≥ target 的长度最小的 连续子数组
        n = len(nums)
        left = right = 0
        res = n+1
        sums = 0
        while right<n:
            sums += nums[right]
            while sums >= target: # 题意
                res = min(res, right - left + 1)  # 记录最小长度
                sums -= nums[left]
                left += 1 # 缩小窗口
            right += 1 # 增加窗口
        return res if res != (n + 1) else 0

    def minSubArrayLen(self, target, nums):
        left, right = 0, 0
        n = len(nums)
        sums = 0 # 区间和
        res = n + 1 # 最小长度, 取一个不存在的数
        while right < n:
            # 还有剩余元素未考察并且窗口内元素总和<目标值target
            sums += nums[right]
            right += 1 # right已经+1过了，所以res=right-left
            # 窗口内的和超过target了,left++,尝试缩小窗口
            # 如果 sums < target，根据题意，right++，一直扩大右区间
            while sums >= target:
                res = min(res, right - left) # 窗口内元素总和>=目标值target则更新结果值
                sums -= nums[left]
                left += 1

        # 该return方法，记忆！
        return res if res != (n+1) else 0


if __name__ == '__main__':
    target = 7
    nums = [2, 3, 1, 2, 4, 3] # [4,3] 2
    print(Solution().minSubArrayLen(target, nums))
    print(Solution().myans(target, nums))
