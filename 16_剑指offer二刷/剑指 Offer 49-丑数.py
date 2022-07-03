"""
middle 一维dp
2021-07-18
"""
# 设置3个索引a, b, c，分别记录前几个数已经被乘2， 乘3， 乘5了，
# 比如a表示前(a-1)个数都已经乘过一次2了，下次应该乘2的是第a个数；
# b表示前(b-1)个数都已经乘过一次3了，下次应该乘3的是第b个数；
# c表示前(c-1)个数都已经乘过一次5了，下次应该乘5的是第c个数；
# https://leetcode-cn.com/problems/chou-shu-lcof/solution/mian-shi-ti-49-chou-shu-dong-tai-gui-hua-qing-xi-t/
class Solution:
    def nthUglyNumber(self, n):
        dp = [1]*n
        a,b,c = 0,0,0
        for i in range(1,n):
            n2,n3,n5 = dp[a]*2,dp[b]*3,dp[c]*5
            dp[i] = min(n2,n3,n5)
            if dp[i]==n2:a+=1
            if dp[i]==n3:b+=1
            if dp[i]==n5:c+=1
        return dp[-1]


if __name__ == '__main__':
    n = 10
    print(Solution().nthUglyNumber(n))