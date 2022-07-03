"""
middle 2021-12-06 2维DP（str中有多少个回文串）
https://programmercarl.com/0647.%E5%9B%9E%E6%96%87%E5%AD%90%E4%B8%B2.html
https://leetcode-cn.com/problems/palindromic-substrings/solution/shou-hua-tu-jie-dong-tai-gui-hua-si-lu-by-hyj8/
dp[i][j]：表示区间范围[i,j] （注意是左闭右闭）的子串是否是回文子串，如果是dp[i][j]为true，否则为false。
1\当s[i]与s[j]不相等，那没啥好说的了，dp[i][j]一定是false。
2\当s[i]与s[j]相等时，有如下三种情况
    2.1、下标i 与 j相同，同一个字符例如a，当然是回文子串；
    2.2、下标i 与 j相差为1，例如aa，也是回文串；
    2.3、下标i 与 j相差大于1的时候，例如cabac，此时s[i]与s[j]已经相同了，
    我们看i到j区间是不是回文子串就看aba是不是回文就可以了，
    那么aba的区间就是 i+1 与 j-1区间，这个区间是不是回文就看dp[i + 1][j - 1]是否为true。
【注意】：矩阵遍历一定要从下到上，从左到右遍历，这样保证dp[i + 1][j - 1]都是经过计算的。
"""
# 2022/03/14 myself
#     def countSubstrings(self, s: str) -> int:
#         n = len(s)
#         if n==1:return n
#         dp=[[False]*n for _ in range(n)]
#
#         res=0
#         for i in range(n):
#             dp[i][i]=True
#             res+=1
#
#         for j in range(1,n):
#             for i in range(0,j):
#                 if s[i]!=s[j]:dp[i][j]=False
#                 else:
#                     if j-i+1<=3 and j-i+1>1:
#                         dp[i][j]=True
#                     else:
#                         dp[i][j]=dp[i+1][j-1]
#                     if dp[i][j]:res+=1
#
#         return res

class Solution(object):
    def countSubstrings(self, s):
        dp = [[False] * len(s) for _ in range(len(s))]
        res = 0
        # 从下到上
        for i in range(len(s)-1, -1, -1):
            # 从左到右
            # 因为dp[i][j]的定义，所以j一定是大于等于i的，那么在填充dp[i][j]的时候一定是只填充右上半部分
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j-i <= 1: # a, aa
                        res += 1
                        dp[i][j] = True
                    elif dp[i+1][j-1]: # cabac
                        res += 1
                        dp[i][j] = True
        return res

if __name__ == '__main__':
    s = "abc"
    myResult = Solution()
    print(myResult.countSubstrings(s))