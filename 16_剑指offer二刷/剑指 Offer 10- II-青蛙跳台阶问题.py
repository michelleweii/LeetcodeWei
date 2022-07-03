"""
dp easy
2021-07-13
https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/solution/mian-shi-ti-10-ii-qing-wa-tiao-tai-jie-wen-ti-dong/
"""
"""
class Solution:
    def numWays(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007
"""
class Solution:
    def numWays(self, n: int):
        if n==0:return 1
        if n==1:return 1
        dp = [1 for _ in range(n+1)]
        for i in range(2, n+1):
            dp[i] = (dp[i-1]+dp[i-2])%1000000007
        return dp[n]


if __name__ == '__main__':
    n = 7
    print(Solution().numWays(n))