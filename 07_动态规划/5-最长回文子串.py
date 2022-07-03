"""
middle 2022-03-03 双指针
思路：从中心向两边扩散
[中心扩展法](https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zui-chang-hui-wen-zi-chuan-by-leetcode-solution/)
[动态规划](https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zhong-xin-kuo-san-dong-tai-gui-hua-by-liweiwei1419/)
"""
"""
middle 2021-12-06 动态规划
相关题目647、132
# dp[i][j] 表示 s[i, j] 是否是回文串
"""
class Solution:
    # 动态规划
    #
    # 1、定义状态
    # dp[i][j] 表示：子串 s[i..j] 是否为回文子串，这里子串 s[i..j] 定义为左闭右闭区间，即可以取到 s[i] 和 s[j]。
    # s[i..j]，所以必然有i<=j

    # 2、状态转移方程
    # dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

    # 3、初始化
    # 单个字符一定是回文串，dp[i][i] = true
    # 看到 dp[i + 1][j - 1] 就需要考虑特殊情况：如果去掉 s[i..j] 头尾两个字符子串 s[i + 1..j - 1] 的长度严格小于2（不构成区间），
    # 即 j−1−(i+1)+1<2 时，整理得 j−i<3，此时 s[i..j] 是否是回文只取决于 s[i] 与 s[j] 是否相等。
    #
    # 结论也比较直观：j−i<3 等价于 j−i+1<4，即当子串s[i..j] 的长度=2 或者=3 的时候，s[i..j] 是否是回文由 s[i] 与 s[j] 是否相等决定。

    def dp(self, s):
        if not s or len(s) == 1: return s
        n = len(s)

        start,maxlen=0,1
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True # 单个字符即回文

        # s[i..j]，所以必然有i<=j
        for j in range(1,n):
            for i in range(0,j):
                if s[i]!=s[j]:
                    dp[i][j]=False
                else: # s[i]==s[j]
                    if j-i+1<=3:
                        dp[i][j]=True # aa, aba
                    else:
                        dp[i][j] = dp[i+1][j-1] # 从两边向里面
                # 只要 dp[i][j] == true 成立，就表示子串 s[i..j] 是回文，此时记录回文长度和起始位置
                if dp[i][j] and j-i+1>maxlen:
                    maxlen = j-i+1
                    start = i
        return s[start:start+maxlen]

    # 双指针（中心扩散）
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s)==1:return s
        start,end=0,0
        for i in range(len(s)):
            # 由于存在奇数的字符串和偶数的字符串，所以我们需要从一个字符开始扩展，或者从两个字符之间开始扩展，所以总共有 n+n-1 个中心。
            left1,right1 = self.expand(s,i,i) # a
            left2,right2 = self.expand(s,i,i+1) # aa
            # print(left1,right1,left2,right2)
            # right1-left1+1 是以i为中心点的最长回文子串
            if right1-left1>end-start:
                start,end=left1,right1
            if right2-left2>end-start:
                start,end=left2,right2
        return s[start:end+1]

    def expand(self, s, left, right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        # return j-i-1
        return left+1,right-1 # 因为最后一次循环多++,--了一次。所以真实回文的位置要恢复




if __name__ == '__main__':
    # s = "babab"
    # 输出："bab"
    # 解释："aba" 同样是符合题意的答案。
    s = "cbbd"
    print(Solution().longestPalindrome(s))
    print(Solution().dp(s))