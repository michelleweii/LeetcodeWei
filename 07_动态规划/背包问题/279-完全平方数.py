"""
middle 2022-03-17 完全背包（不带顺序）
# dp[i]：表示完全平方数和为i的 最小个数
https://leetcode.cn/problems/perfect-squares/solution/by-flix-sve5/
"""
class Solution:
    # 不要求顺序的完全背包13=4+9，13=9+4
    def numSquares(self, n: int):# -> int:
        # 预处理出 <=sqrt(n) 的完全平方数
        nums = []
        i = 1
        while i * i <= n:
            nums.append(i * i)
            i += 1

        # 构成数字i所需的最少完全平方数个数
        dp=[n]*(n+1) # n是target
        dp[0]=0
        for num in nums:  # 物品体积
            for i in range(num,n+1): # 背包容量
                dp[i]=min(dp[i],dp[i-num]+1) # 不选num，选num
        return dp[n]
    
if __name__ == '__main__':
    n = 12
    print(Solution().numSquares(n)) # 4+4+4 3个