"""
hard 2维DP
2021-07-25
dp[i][j] s的前i和字母和p的前j个字母能够匹配
dp[i][j] 代表 A 的前 i 个和 B 的前 j 个能否匹配
https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/solution/zhu-xing-xiang-xi-jiang-jie-you-qian-ru-shen-by-je/
"""
class Solution:
    def isMatch(self, s: str, p: str):
        n = len(s)
        m = len(p)
        dp = [[False for _ in range(m+1)] for _ in range(n+1)] # n行m列
        dp[0][0] = True # 空串和空模式串是匹配的， 空模式串和任意的
        for i in range(n+1):
            for j in range(m+1):
                if j == 0:
                    dp[i][j] = i == 0
                else:
                # 非空正则分为两种情况 * 和 非*
                    if p[j-1] != '*':
                        if i>0 and ((s[i-1]==p[j-1]) or p[j-1]=='.'):
                            dp[i][j] = dp[i-1][j-1]
                    else:
                        # 不看
                        if j>=2:
                            dp[i][j] |= dp[i][j-2]
                        # 看
                        if i>=1 and j>=2 and ((s[i-1] == p[j-2]) or p[j-2]=='.'):
                            dp[i][j] |= dp[i-1][j]
        # print(dp)
        return dp[-1][-1]


if __name__ == '__main__':
    # s = "aa"
    # p = "a"
    # s = "mississippi"
    # p = "mis*is*p*."
    s = "mississippi"
    p = "mis*is*ip*."
    print(Solution().isMatch(s, p))