# -*- coding:utf-8 -*-
class Solution:
    # 从0开始，第0项为0
    def Fibonacci(self, n):
        if n<=0:return 0
        if n<=2:return 1
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        print(dp)
        return dp[n]

if __name__ == '__main__':
    n = 5
    print(Solution().Fibonacci(n))