"""
easy 一维dp入门题目
"""
class Solution(object):
    def fib(self, n):
        if not n:return 0
        dp = [0 for _ in range(n+1)]
        dp[0]=0
        dp[1]=1
        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]

if __name__ == '__main__':
    N = 4
    print(Solution().fib(N))
