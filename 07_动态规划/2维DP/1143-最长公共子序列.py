"""
middle 2021-07-12 2维DP
https://leetcode-cn.com/problems/longest-common-subsequence/solution/fu-xue-ming-zhu-er-wei-dong-tai-gui-hua-r5ez6/
dp[i][j]: text1前i个字符和text2前j个字符，所能构成的最长公共序列。
"""
class Solution:
    def longestCommonSubsequence(self, text1, text2):
        if not text1 or not text2:return 0
        len1,len2=len(text1),len(text2)
        # dp[i][j], 所有text1[0-(i-1)], text2[0-(j-1)]的公共子序列集合，max。
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[len1][len2]
# 举个例子，比如对于 ace 和 bc 而言，
# 他们的最长公共子序列的长度等于 ① ace 和 b 的最长公共子序列长度0;
# ② ac 和 bc 的最长公共子序列长度1 的最大值，即 1。
if __name__ == '__main__':
    text1 = "abc"
    text2 = "ab"
    print(Solution().longestCommonSubsequence(text1, text2))