# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # 要求输出循环左移3位后的结果
        s = s[::-1]
        # print(s)
        b= s[:len(s)-n-1:-1]
        # print(b)
        a = s[len(s)-n-1::-1]
        # print(a)
        return a+b


if __name__ == '__main__':
    s = "XYZdefabc"
    n = 3
    print(Solution().LeftRotateString(s,n))