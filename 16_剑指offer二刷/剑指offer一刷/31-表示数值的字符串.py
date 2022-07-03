# -*- coding:utf-8 -*-
class Solution:
    # E,e前后都要有东西
    # 小数点只能出现一次
    # +，-只能出现在s[0]或是e，E的后面
    def isNumeric(self, s):
        # write code here
        s = s.replace(" ","")
        if not s or (s[0]=='.' and len(s)==1):return False
        if s.count('.')>1 or s.count('e')>1 or s.count('E')>1 \
                or s.count('+')>2 or s.count('-')>2:return False

        if s[0] in '+-':s=s[1:]
        dot, e = 0, 0
        i, n = 0, len(s)
        while i < n:
            if s[i]=='.' and e:
                return False
            elif s[i]=='e' or s[i]=='E':
                e += 1
                if i==0 or i == n-1:
                    return False
                if s[i+1]=='+' or s[i+1]=='-':
                    if i+2==n:
                        # print(i+2)
                        # print(i, s[i])
                        return False
                    i += 1
            elif s[i]!='.' and s[i] not in "0123456789":
                return False
            i += 1
        return True


"""
定义两个标志位，分别表示E或者e是否出现过，以及小数点.是否出现过。 
1. 以e（或E）为分隔，获得两个子字符串；e之前的字符串小数点只能出现一次；e之后的字符串不允许出现小数点； 
2. 符号位+或-只可能出现在两个子字符串的首位； 
3. e（或E）、小数点.不能出现在末尾
"""

if __name__ == '__main__':
    # s = "-1E-16 "
    s = " 1a3.14"
    s = "123.45e+6"
    print(Solution().isNumeric(s))