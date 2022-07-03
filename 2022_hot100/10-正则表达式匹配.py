"""
hard 2021-12-08 2维DP
同剑指 Offer 19-正则表达式匹配
状态：dp[i][j] 表示 s 的前 i 个是否能被 p 的前 j 个匹配
https://leetcode-cn.com/problems/regular-expression-matching/solution/shou-hui-tu-jie-wo-tai-nan-liao-by-hyj8/
"""
# 特例
# s = "ab" p = ".*" True（.是任意字符，不是说选定一个字符就不会变了，*只是增加.的个数，看作..之后再转化为ab）
# s = ""  p = ".*" True（*可以匹配0到多个前一个字母）
# *必须和字母或者'.'配合使用，不能独立存在

# *前出现0次，dp[i][j]=dp[i][j-2]
# *前出现1次，dp[i][j]=dp[i-1][j-2]
# *前出现多次，dp[i][j]=dp[i-1][j]
class Solution(object):
    def isMatch(self, s, p):
        if not s or not p:return False
        s_len, p_len = len(s), len(p)
        # s、p 串是否匹配，取决于：最右端是否匹配、剩余的子串是否匹配
        # dp[i][j]:表示s的前i个字符，p的前j个字符是否能够匹配
        dp = [[False] * (p_len+1) for _ in range(s_len+1)]
        # 出口，用p的前0个字符去匹配s的前0个字符
        # 1、s为空，p为空，能匹配上
        dp[0][0] = True
        # 2、p为空，s不为空，必为false(boolean数组默认值为false，无需处理)
        # 3、s为空，p不为空，由于*可以匹配0个字符，所以有可能为true
        """
        base case
        p为空串，s不为空串，肯定不匹配。
        - s为空串，但p不为空串，要想匹配，只可能是右端是星号，它干掉一个字符后，把 p 变为空串。
        s、p都为空串，肯定匹配。
        """
        for j in range(1, p_len+1):
            if p[j-1]=='*': dp[0][j] = dp[0][j-2]

        # 4、填表
        for i in range(1, s_len+1):
            for j in range(1, p_len+1):
                # dp[i][j]:s的前i个字符s[0:i-1]与p的前j个字符p[0:j-1]是否匹配
                if s[i-1]==p[j-1] or p[j-1]=='.':
                    dp[i][j] = dp[i-1][j-1]
                # *特判, *可以让它前面的字符出现0-n次
                if p[j-1]=='*':
                    if s[i-1]==p[j-2] or p[j-2]=='.':
                        # dp[i][j] = dp[i-1][j-2] # *让它前面的字符出现1次,  aa与a*以及 aa与.* ,dp[i-1][j-2]
                        # dp[i][j] = dp[i-1][j-3] # *让它前面的字符出现0次， aa与aac* ,dp[i][j-2]
                        # 还可以dp[i][j] = dp[i][j-2]
                        # dp[i][j] = dp[i-1][j] # *让它前面的字符出现多次， aaaaaaa与a*
                        dp[i][j] = dp[i][j-2] or dp[i-1][j-2] or dp[i-1][j]
                    elif s[i-1]!=p[j-2]: # a与ab*, 干掉b
                        dp[i][j] = dp[i][j-2]

        return dp[s_len][p_len]


"""
调包
    import re
    # re.match(pattern, string, flags=0)
    # pattern	匹配的正则表达式
    # string	要匹配的字符串（长的）
    # re.I不区分大小写
    match = re.match(p, s, re.I)
    # 匹配成功re.match方法返回一个匹配的对象，否则返回None。
    #
    # 我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。
    print(match) # <_sre.SRE_Match object; span=(0, 1), match='a'>
    print(match.group())  # a
    if match is not None:
        return match.group() == s
    elif match is None:
        return s == None
    else:
        return False
"""

if __name__ == '__main__':
    # s = "a"
    # p = "a*"
    # s = "ab"
    # p = ".*"
    s = "mississippi"
    p = "mis*is*p*."
    print(Solution().isMatch(s,p))