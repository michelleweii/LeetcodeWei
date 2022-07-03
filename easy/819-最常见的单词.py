# Python中字符串自带的split方法一次只能使用一个字符对字符串进行分割，但是python的正则模块则可以实现多个字符分割
# 我的思路：
# 通过split将每个单词划分开，在用字典遍历存储每一个单词，如果单词是ban的话，就不进入字典。
# pycharm正确，但是leetcode无法通过。


import re
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # a = 'one1two2three3four4five5'
        # print(re.split('\d+', a))

        # para = paragraph.split(",")
        # print(para)
        para = re.split(" |,|\.|\s+",paragraph.lower())
        # print(para)
        ban = "".join(banned)
        # print(ban)
        dict = {}
        # print(ban)
        # assert ban==
        for i in para:
            # print(i)
            if i==ban:
                continue
            if i not in dict.keys():
                dict[i] = 1
            else:
                count = dict[i]
                count += 1
                dict[i]=count
        # print(dict)
        maxlen = max(i for i in list(dict.values()) if i!='')
        for key,value in dict.items():
            if value == maxlen:
                return str(key)


def main():
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    myResult = Solution()
    print(myResult.mostCommonWord(paragraph, banned))

if __name__ == '__main__':
    main()

"""
def mostCommonWord(self, paragraph, banned):
    ban = set(banned)
    paragraph = [s.strip("!?',;.") for s in paragraph.lower().split(' ')]
    p = [w for w in paragraph if w not in ban]
    word_count = {w: 0 for w in p}
    for w in p:
        word_count[w] += 1
    return max(word_count, key=lambda k: word_count[k])
"""