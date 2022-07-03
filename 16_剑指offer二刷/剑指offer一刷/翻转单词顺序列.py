# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        s = s.split(' ')
        s.reverse()
        s = " ".join(s)
        return s

if __name__ == '__main__':
    s = "student. a am I"
    print(Solution().ReverseSentence(s))

    # I am a student.