"""
hard
哈希表+双指针
https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-w-6/
o(n*mw)
枚举所有子串的开头，从这个单词开始，查看所有的[i,i+w,i+2w,...,i+(m-1)w)，
判断单词是否已经用过了，这个单词是否和hashmap中的一致
o(n*w)
[i,i+w,i+2w,...,i+(m-1)w),[i+(m-1)w), [i+(m-1)w, i+mw)
i=0, w, 2w, 3w,...
i=1, w+1, ...
...
i=w-1
"""
# 感觉和76挺像的, 每次比较一个子串的长度！
# 需要2个hashmap
# hashmap1 原始words target中每个单词个数
# hashmap2 保存子串单词且子串单词在hashmap1中，如果hashmap2中某单词的个数>hashmap1中这个单词的数量，说明匹配失败
# 匹配失败，接着匹配下一个子串
# 匹配成功，继续判断下一个单词的情况
from collections import Counter  ######
class Solution:
    def findSubstring(self, s, words):
        """
        利用字典存储words中每个单词及其出现次数
        由于每个单词长度(w_l)一样，个数为m，则采用宽度为 m * w_l 的滑动窗口
        每次只需判断滑动窗口中单词(每w_l长度的字符串算作一个单词)的出现次数是否与words中的一样
        """
        res = []
        n = len(s)
        words_num = len(words) # 给定单词list的长度, 时间复杂度于此无关
        word_len = len(words[0]) # 每个单词的长度
        words_map = Counter(words) # hashmap1存target的所有单词
        # print(words_map) # Counter({'foo': 1, 'bar': 1})
        # wordsMap = {}
        # for word in words: wordsMap[word] = wordsMap.get(word, 0) + 1
        # print(wordsMap) # {'foo': 1, 'bar': 1}
        # 开始遍历所有子串
        for i in range(n-word_len*words_num+1):
            num = 0
            win_map = {} #
            # 判断子串是否符合
            while num<words_num: # len(["foo", "bar"])
                word = s[i+num*word_len:i+(num+1)*word_len] # word_len=3 0:3, 3:6
                # print(word)
                """
                扫描子串的单词，如果当前扫描的单词在之前的 HashMap1 中，
                就把该单词存到新的 HashMap2 中，并判断新的 HashMap2 中该单词的 value 是不是大于之前的 HashMap1 该单词的 value ，
                如果大了，就代表该子串不是我们要找的，接着判断下一个子串就可以了。如果不大于，那么我们接着判断下一个单词的情况。
                """
                # 判断该单词是否in hashmap1
                if word in words_map:
                    win_map[word] = win_map.get(word,0)+1
                    # print(win_map)
                else:break
                # 判断当前单词的 value 和 HashMap1 中该单词的 value，当前子串不合格
                if win_map.get(word)>words_map.get(word):break
                num+=1 # 每匹配完words里面的一个字符串之后将计数加一
            # 判断是不是所有的单词都符合条件
            if num==words_num:
                res.append(i)
        return res

if __name__ == '__main__':
    # s = "barfoothefoobarman"
    # words = ["foo", "bar"]
    s="wordgoodgoodgoodbestword"
    words=["word", "good", "best", "word"] # [0,4,8]
    print(Solution().findSubstring(s, words))
    # [0,9]

    # s = "wordgoodgoodgoodbestword", words = ["word", "good", "best", "word"]
    # []