"""
middle 2022-05-05 dp（pdd面筋）
https://leetcode-cn.com/problems/arithmetic-slices/solution/hua-dong-chuang-kou-dong-tai-gui-hua-jav-3vpp/
题目：返回nums中所有为等差数组的 子数组 个数。至少3个元素。
子数组要连续！！！

状态定义：dp[i] 表示：以 nums[i] 结尾的、且长度大于等于 3 的连续等差数列的个数。这个定义比较长，拆解一下：
- 必需以 nums[i] 结尾，nums[i] 必需被选取；
- 长度大于等于 3；
"""
class Solution:
    def numberOfArithmeticSlices(self, nums): #List[int]) -> int:
        n = len(nums)
        if n<3:return 0
        dp = [0]*n #  表示以：nums[i] 结尾的、且长度大于等于 3 的连续等差数列的个数
        res = 0
        # 从下标 2 开始，才有可能构成长度至少大于等于 3 的等差数列
        for i in range(2,n):
            # 隐含了判断等差数列的长度大于等于 3
            if nums[i]-nums[i-1]==nums[i-1]-nums[i-2]:
                dp[i]=dp[i-1]+1
                res+=dp[i]
        return res

if __name__ == '__main__':
    nums = [1,2,3,4]
    print(Solution().numberOfArithmeticSlices(nums))

