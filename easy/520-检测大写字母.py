# -*- coding:utf-8 -*-
"""
给定一个单词，你需要判断单词的大写使用是否正确。我们定义，在以下情况时，
单词的大写用法是正确的：全部字母都是大写，比如"USA"。单词中所有字母都不是大写，
比如"leetcode"。如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。
否则，我们定义这个单词没有正确使用大写字母。
"""

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        count_b = 0
        for i in word:
            if(ord(i)>=65 and ord(i)<=90):  # 如果是大写字母
                count_b+=1
        if(count_b==len(word) or count_b==0): # 全是小写或者全是大写
            return True
        if(count_b==1 and ord(word[0])>=65 and ord(word[0])<=90): # 如果只有第一个字母是大写
            return True

        else:
            return False

def main():
    word = "a"
    rs = Solution()
    print(rs.detectCapitalUse(word))

if __name__ == '__main__':
    main()
