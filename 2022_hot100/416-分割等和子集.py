"""
middle 2021-12-14 dp(01背包)
01 背包，即数组中的元素不可重复使用，外循环遍历 arrs，内循环遍历 target，且内循环倒序。
【从2维到1维】https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/0-1-bei-bao-wen-ti-xiang-jie-zhen-dui-ben-ti-de-yo/
https://leetcode-cn.com/problems/coin-change/solution/yi-tao-kuang-jia-jie-jue-bei-bao-wen-ti-h0y40/
"""
# 题目等价于：是否可以从输入数组中挑选出一些正整数，使得这些数的和 等于 整个数组元素的和的一半。
# target 是什么？sum//2
# 是否可以将这个数组分割成两个子集，使得两个子集的元素和相等
# dp[i] 表示是否存在和为 i 的 组合。
class Solution:
    def canPartition(self, nums):
        sum = 0
        for num in nums:
            sum+=num
        # 特判：如果是奇数，就不符合要求
        if sum%2==1:return False
        target = sum//2
        # 01背包--dp[i][j]表示从数组的 [0, i] 这个子区间内挑选一些正整数，
        # 每个数只能用一次，使得这些数的和恰好等于 j
        dp = [False for _ in range(target+1)]
        dp[0] = True # 什么都不取 # dp[i] 表示是否存在和为 i 的 组合
        # 【模板】外循环遍历 arrs，内循环遍历 target，且内循环倒序
        for x in nums: # 遍历物品体积
            for j in range(target, x-1, -1): #j>=x # 遍历背包容量，背包容量必然要>=物品体积
                dp[j] = dp[j] or dp[j-x] # 不选or选
        return dp[target]
"""
    def canPartition(self, nums: List[int]) -> bool:
        sum = 0
        for num in nums:
            sum += num
        if sum & 1:
            return False
        target = sum // 2
        n = len(nums)

        dp = [False for _ in range(target + 1)]

        # 依据状态定义做判断:
        # 因为下标[0,0]中nums[0]凑不出0所以设置成False
        # 如果依据状态转移则可以理解为:
        # [j - nums[i]] == 0 表示nums[i]恰好为一组,其余为一组,刚才凑成,所以True没问题
        dp[0] = True

        # 先填表格第 0 行，第 1 个数只能让容积为它自己的背包恰好装满
        if nums[0] <= target:
            dp[nums[0]] = True
        
        for i in range(1, n): # 选数
            for j in range(target, -1, -1):
                #「从后向前」 写的过程中，一旦 nums[i] <= j 不满足，可以马上退出当前循环
                # 因为后面的 j 的值肯定越来越小，没有必要继续做判断，直接进入外层循环的下一层。
                # 相当于也是一个剪枝，这一点是「从前向后」填表所不具备的。
                if nums[i] <= j: # nums[i]是物品体积，j是背包容量
                    dp[j] = dp[j] or dp[j - nums[i]]
                else:
                    break
        return dp[-1]
"""
if __name__ == '__main__':
    nums = [1, 2, 3, 5] # f
    print(Solution().canPartition(nums))