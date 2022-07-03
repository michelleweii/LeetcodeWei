# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        if not s or len(s)>=10000:
            return -1
        for ch in s:
            if s.count(ch)==1:
                return s.index(ch)




if __name__ == '__main__':
    s = "google"
    print(Solution().FirstNotRepeatingChar(s))