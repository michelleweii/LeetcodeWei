"""
hard 2021-12-06 2维DP（腾讯）
https://leetcode-cn.com/problems/distinct-subsequences/solution/shou-hua-tu-jie-xiang-jie-liang-chong-ji-4r2y/
https://leetcode-cn.com/problems/distinct-subsequences/solution/shu-ju-jie-gou-he-suan-fa-dong-tai-gui-h-6ney/
"""
# 2021/12/06 还是有点不明白
# 尾部字符成功匹配上了，dp[i][j] = dp[i-1][j-1] + dp[i-1][j] # 为什么还要加没有配上的case呢？
# https://leetcode-cn.com/problems/distinct-subsequences/solution/shu-ju-jie-gou-he-suan-fa-dong-tai-gui-h-6ney/
# 题目：求 s 的子序列中 t 出现的个数，blabla...
# 翻译：在 s 串身上 “挑选” 字符，去匹配 t 串的字符，求挑选的方式数
# 抓住 “选”，s 要照着 t 来挑选(用s去匹配t)，逐字符考察选或不选，分别来到什么状态？

# dp[i][j]状态定义：从开头到s[i-1]的子串中，出现『从开头到t[j-1]的子串』的 次数。
# 即：前 i 个字符的 s 子串中，出现前 j 个字符的 t 子串的次数。

# dp出口
# 1) 小到 t 变成空串，此时 s 为了匹配它，方式只有1种：什么字符也不用挑（或 s 也是空串，什么都不做就匹配了，方式数也是1）
# 2) 小到 s 变成空串，但 t 不是，s 怎么也匹配不了 t，方式数为 0
class Solution:
    def numDistinct(self, s: str, t: str):
        s_len = len(s)
        t_len = len(t)
        dp = [[0 for ti in range(t_len+1)] for si in range(s_len+1)] # s行t列

        for i in range(s_len+1):
            for j in range(t_len+1):
                if j==0:dp[i][j] = 1
                # elif i==0:dp[i][j] = 0
                else:
                    if s[i-1] == t[j-1]:
                        # 核心是选or不选
                        # 最后一个字符可以匹配
                        # 情况一：用s的第i个字母匹配t的第j个字符，有 dp[i-1][j-1] 个匹配情况；
                        # 情况二：不用s的第i个字母去匹配t的第j个字母, 情况就等于 dp[i-1][j]；
                        dp[i][j] = dp[i-1][j-1] + dp[i-1][j] # 为什么还要加没有配上的case呢？
                    else:
                        # 从s中挑选，最后一个字符不匹配，那么这个字符有和没有情况是一样的
                        dp[i][j] = dp[i-1][j]

        return dp[-1][-1]

if __name__ == '__main__':
    s = "babgbag"
    t = "bag"
    print(Solution().numDistinct(s,t))