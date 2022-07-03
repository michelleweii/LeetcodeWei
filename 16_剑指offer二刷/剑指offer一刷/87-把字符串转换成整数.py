# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        if not s:return 0
        k = 0
        while k<len(s) and s[k]==' ':k+=1
        num = 0
        is_minus = False
        if s[k] == '+': k += 1
        elif s[k] == '-':
            k += 1
            is_minus = True
        while k<len(s) and s[k]>='0' and s[k]<='9':
            # num = num*10+(ord(s[k])-48)
            num = num*10+(ord(s[k])-ord('0'))
            k+=1
        if k!=len(s):return 0
        if is_minus:
            num *= -1
        return num

if __name__ == '__main__':
    s = '1a33'
    print(Solution().StrToInt(s))