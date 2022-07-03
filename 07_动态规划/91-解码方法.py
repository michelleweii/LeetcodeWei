"""
middle 2022-01-24 dp
(这种方案的好处就是没有技巧，但是判断多)https://leetcode-cn.com/problems/decode-ways/solution/chao-xiang-xi-cong-bao-li-di-gui-dao-don-6vwr/
https://leetcode-cn.com/problems/decode-ways/solution/gong-shui-san-xie-gen-ju-shu-ju-fan-wei-ug3dd/
【核心】对于字符串 s 的某个位置 i 而言，我们只关心「位置 i 自己能否形成独立 item 」
和「位置 i 能够与上一位置（i-1）能否形成 item。
状态定义：以字符串s[i]作为结尾的解码方案数。即定义 dp[i] 为考虑前 i 个字符的解码方案数。
"""
# 实际上有两个约束条件，1. 0不能单独解码 2. 两位数必须在1与26之间。
# 这道题目实际上是用DP去做，仔细想的话，可以发现就是约束版的f(n) = f(n-1) + f(n-2);
# 其中如果是s[n-1]为0，f(n-1) = 0，f(n) = f(n-2)，
# 因为0无法单独解码，而f(n-2)的条件则是必须在1与26之间，否则f(n) = f(n-1)。

"""
s[i-2]和s[i-1] 两个字符是10----26之间但不包括10和20这两个数时，有两种编码方式，比如23------>[“BC”，“W”]，所以dp[i] = dp[i-1]+dp[i-2]
s[i-2]和s[i-1] 两个字符10或20这两个数时，有一种编码方式，比如10------>[“J”], 所以dp[i] = dp[i-2]
s[i-2]和s[i-1] 两个字符不在上述两种范围时，编码方式为零，比如27，比如01，所以dp[i] = dp[i-1
"""
class Solution:
    def numDecodings2(self, s):
        if s[0] == '0': return 0 # 前导0为无效
        if len(s) == 1: return 1
        legalstr = set(str(i) for i in range(1, 27)) # 合法集合
        # print(legalstr)
        dp = [0] * (len(s))
        dp[0] = 1 # s[0]只有一种方案数
        if s[1] not in legalstr:  # s[1]为0时，只能和s[0]进行组合。
            dp[1] = 1 if s[: 2] in legalstr else 0
        else: # s[1]不是0时，可以组合，可以单独出结果
            dp[1] = 2 if s[: 2] in legalstr else 1
        # 因为要用到i-2 所以至少初始化 dp[0] dp[1]
        for i in range(2, len(s)):
            if s[i] not in legalstr:
                # 向前一位组合
                if s[i - 1: i + 1] in legalstr:
                    dp[i] = dp[i-2]
            else:
                if  s[i - 1: i + 1] in legalstr:
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]

        return dp[-1]


    def numDecodings(self, s):
            if s == "" or s[0]=='0': return 0
            dp = [1,1]
            for i in range(2,len(s)+1):
                if 10 <=int(s[i-2:i]) <=26 and s[i-1]!='0':#编码方式为2
                    dp.append(dp[i-1]+dp[i-2])
                elif int(s[i-2:i])==10 or int(s[i-2:i])==20:#编码方式为1
                    dp.append(dp[i-2])
                elif s[i-1]!='0':#编码方式为0
                    dp.append(dp[i-1])
                else:
                    return 0
            #print(dp[len(s)])
            return dp[len(s)]
    
if __name__ == "__main__":
    print(ord('1'))
    s = "12"
    print(Solution().numDecodings2(s))