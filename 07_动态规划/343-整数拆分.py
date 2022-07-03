"""
middle 2022-05-03 一维动态规划
https://leetcode-cn.com/problems/jian-sheng-zi-lcof/solution/jian-zhi-offer-14-i-jian-sheng-zi-dong-t-c7ou/
解题思路
设数组dp记录0 ~ n 剪绳子的最大乘积
两层遍历：第一层i表示绳子的长度; 第二层j用来表示第一段减去的长度。要想求最大值，有两种情况：
- 剪绳子：剪绳子的话乘积就是 j * dp[i - j]， 减去第一段的长度 * 剩下长度的最大值【剩下(i - j)长度可以剪也可以不剪，剪】
        剪第一段，第二段不剪，直接 j * (i - j ) 当前的长度 * 剩下的长度【剩下(i - j)长度可以剪也可以不剪，不剪)】
- 不剪 dp[i]

状态定义：dp[i]表示长度为i的绳子剪成m段后的最大乘积。初始化dp[2] = 1。
第一段长度j可以取的区间为[2,i)。

因为剪1段对乘积无帮助，1*（n-1）还变小了。
"""
class Solution:
    def cuttingRope(self, n: int):# -> int:
        dp=[0]*(n+1) # 数组dp记录0~n 剪绳子的最大乘积
        dp[2]=1
        for i in range(3,n+1): # 遍历绳子的长度i
            for j in range(1,i//2+1): # 剪去的长度j
                dp[i]=max(dp[i], max(j*(i-j), j*dp[i-j]))

        return dp[n]

if __name__ == '__main__':
    n = 10
    print(Solution().cuttingRope(n))