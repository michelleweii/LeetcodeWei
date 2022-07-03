"""
middle 2021-12-14 2维DP（腾讯、虾皮、快手）
dp[i][j]表示 s1 的前i个(s1[i-1])个字符和s2的前j个(s2[j-1])字符是否能构成 s3 的前i+j个字符。
https://leetcode-cn.com/problems/interleaving-string/solution/dong-tai-gui-hua-zhu-xing-jie-shi-python3-by-zhu-3/
多初始化一维是为了放置空字符，看链接里的图例。
状态转移方程：
dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) \ # s1最后一个字符和s3最后一个字符匹配
        or (dp[i][j-1] and s2[j-1] == s3[i+j-1]) # s2最后一个字符和s3最后一个字符匹配
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1,len2,len3 = len(s1),len(s2),len(s3)
        if len1+len2 != len3:return False
        # dp[i][j]表示 s1 的前i个(s[i-1])个字符和 s2 的前j个字符是否能构成 s3 的前i+j个字符。
        dp = [[False for i in range(len2+1)] for j in range(len1+1)] # lens1行，lens2列
        # 定义出口
        dp[0][0] = True # s1的0个字符，s2的0个字符，当然可以构成s3的0个字符

        # 1、只由s1构成s3 # s1的前i位是否能构成s3的前i位
        for i in range(1, len1+1):
            # s1的前i位能构成s3的前i位的前提条件是：
            # 前i-1位可以构成s3的前i-1位，且s1的第i位（s1[i-1]）等于s3的第i位（s3[i-1]）
            dp[i][0] = dp[i-1][0] and s1[i-1]==s3[i-1]
        # 2、只由s2构成s3  # s2的前i位是否能构成s3的前i位
        for j in range(1, len2+1):
            # 前i-1位可以构成s3的前i-1位，且s2的第i位（s2[i-1]）等于s3的第i位（s3[i-1]）
            dp[0][j] = dp[0][j-1] and s2[j-1]==s3[j-1]
        # 3、填表
        # 状态转移方程
        # s1的前i位和s2的前j位能否构成s3的前i+j(i+j-1)位，取决于2种情况：
        # s1 的前 i 个字符和 s2 的前 j-1 个字符能否构成 s3 的前 i+j−1 位，
        # 且 s2 的第 j 位（s2[j−1]）是否等于 s3 的第 i+j 位（s3[i+j-1]）
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                # s1 的前 i 个字符和 s2 的前 j−1 个字符能否构成 s3 的前 i+j−1 位，# （s1最后一个字符和s3最后一个字符匹配）
                # or s2 的第 j 位（s2[j−1]）是否等于 s3 的第 i+j 位（s3[i+j−1]）。# （s2最后一个字符和s3最后一个字符匹配）
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) \
                           or (dp[i][j-1] and s2[j-1] == s3[i+j-1])

        return dp[-1][-1] # return dp[len1][len2]

# v1.1 2021-11-08
if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(Solution().isInterleave(s1,s2,s3))


# dp[i][j]= (dp[i][j-1] and s2[j-1]==s3[i+j-1]) or
# (dp[i-1][j] and s1[i-1]==s3[i+j-1])
# 解释：s1 前i位和 s2 的前j位能否组成 s3 的前 i+j 位取决于两种情况：
#
# s1的前 i 个字符和 s2 的前 j-1个字符能否构成 s3 的前 i+j-1 位，
# 且 s2 的第 j 位（s2[j-1]）是否等于 s3 的第 i+j 位（s3[i+j-1]）。
