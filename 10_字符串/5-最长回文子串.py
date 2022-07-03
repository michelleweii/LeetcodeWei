"""
middle
简单思路：
首先枚举中心点，向两边枚举，看能枚举多长（两头对应字符串不同）。
分串是奇数or偶数
--------------------------------------------------
马拉车算法——Manacher 算法 o(n)
思路：现将字符串通过添加特定字符'#'，变成奇数个数。
对新字符串使用中心扩展发即可，中心扩展法得到的半径就是子串的长度。

举例：
先转化字符串'35534321'---->'#3#5#5#3#4#3#2#1#'，
然后求出以每个元素为中心的最长回文子串的长度。
"""

class Solution(object):
    # 直观做法
    # 分奇数or偶数开始校验回文串
    def longestPalindrome(self,s):
        lens = 0
        res = ""
        for k in range(len(s)):
            # 奇数
            i = k
            j = k+1
            while(i>=0 and j<len(s) and s[i]==s[j]):
                i-=1
                j+=1
            if (j-i-1) > lens:
                lens = j-i-1
                print(i,j)
                res = s[i+1:j]

            # 偶数
            i = k-1
            j = k+1
            while(i>=0 and j<len(s) and s[i]==s[j]):
                i-=1
                j+=1
            if (j-i-1) > lens:
                lens = j-i-1
                res = s[i+1:j]
        return res

    # 马拉车算法
    def longestPalindrome_plus(self, s):
        s = '#' + '#'.join('{}'.format(s)) + '#'
        lens=len(s)
        max_str = ""
        max_length = 0
        for i in range(lens):
            cur_length,cur_str = self.getLength(s,i)
            if cur_length>max_length:
                max_length = cur_length
                max_str = cur_str
        return max_str.replace('#','')

    def getLength(self,s,index):
        length = 0
        string = s[index]
        for i in range(1,index+1):
            # 从index开始的原因是：从当前词开始向两边扩散
            if i+index<len(s) and s[index-i]==s[index+i]:
                length+=1
                string = s[index-i:index+i]
            else:
                break
        return length,string



if __name__ == '__main__':
    s = "babad"
    myResult = Solution()
    print(myResult.longestPalindrome(s))