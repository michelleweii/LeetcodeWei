"""
easy 2021-12-15 dp
题目：计算从 0 到 n 的每个整数的二进制表示中的 1 的数目
https://leetcode-cn.com/problems/counting-bits/solution/hen-qing-xi-de-si-lu-by-duadua/
思路：
0的二进制0个,dp[0]=0
数字分为奇数、偶数，
针对奇数有：二进制表示中，奇数一定比前面那个偶数多一个 1，因为多的就是最低位的 1。
#           举例：
#          0 = 0       1 = 1
#          2 = 10      3 = 11
针对偶数有：二进制表示中，偶数中 1 的个数一定和除以 2 之后的那个数一样多。因为最低位是 0，
除以 2 就是右移一位，也就是把那个 0 抹掉而已，所以 1 的个数是不变的。
#            举例：
#           2 = 10       4 = 100       8 = 1000
#           3 = 11       6 = 110       12 = 1100
"""
class Solution:
    def countBits(self, n): #int) -> List[int]:
        dp = [0]*(n+1) # 状态定义：数字i的二进制中含dp[i]个1。
        # 根据奇偶性开始遍历计算
        for i in range(1,n+1):
            # 如果是奇数
            if i%2==1:
                dp[i]= dp[i-1]+1
            # 如果是偶数
            else:
                dp[i] = dp[i//2]
        return dp

if __name__ == '__main__':
    n = 5 # [0, 1, 1, 2, 1, 2]
    print(Solution().countBits(n))