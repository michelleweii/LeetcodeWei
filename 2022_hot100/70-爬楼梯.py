"""
easy 2022-01-24 完全背包
https://leetcode-cn.com/problems/climbing-stairs/solution/hua-jie-suan-fa-70-pa-lou-ti-by-guanpengchn/
dp[i]：爬到有i个台阶的楼顶，有dp[i]种方法。
"""
class Solution(object):
    def climbStairs(self, n):
        # 动态规划求解，两个if判断是我之前没想到的，
        # 当n==1的时候，我dp[1]=2就是越界，之前没考虑到。
        # if n==0:
        #     return 0
        # if n==1:
        #     return 1
        # dp = [0 for _ in range(n)]
        # dp[0] = 1
        # dp[1] = 2
        # for i in range(2,n):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n-1]
        if n<=2:return n
        dp = [0]*(n+1) # 爬到有i个台阶的楼顶，有dp[i]种方法。
        dp[1] = 1 # 1阶台阶,只有一种方式(1)
        dp[2] = 2 # 2阶台阶,有两种方式(1+1, 2)
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2] # 可以爬 1 或 2 个台阶
        return dp[n]


        # 递归求解，但超出时间限制
        # if n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        # else:
        #     return (self.climbStairs(n-1)+self.climbStairs(n-2))

if __name__ == '__main__':
    n = 5
    print(Solution().climbStairs(n))