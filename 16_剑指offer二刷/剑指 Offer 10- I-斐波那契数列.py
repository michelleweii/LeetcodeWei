"""
df 斐波那契 easy
2021-07-13
"""
class Solution:
    # 求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）
    def fib(self, n):
        if n==0:return 0
        if n==1:return 1
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = (dp[i-1]+dp[i-2])% 1000000007
        return dp[n]


if __name__ == '__main__':
    n = 5
    print(Solution().fib(n))