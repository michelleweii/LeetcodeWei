# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        dp = [0] * (number+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, number+1):
            dp[i] = dp[i-1] + dp[i-2]
        # print(dp)
        return(dp[-1])


"""
    def jumpFloor(self, n):
        # write code here
        res=[1,1,2]
        while len(res)<=n:
            res.append(res[-1]+res[-2])
        return res[n]
"""

if __name__ == '__main__':
    n = 3
    print(Solution().jumpFloor(n))
