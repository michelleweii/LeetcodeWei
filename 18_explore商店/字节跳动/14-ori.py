"""
easy 2021-10-17 纵向遍历
# python zip特性
"""
class Solution:
    # 纵向遍历
    # i 单词的每一位
    # j 每一个单词
    def longestCommonPrefix(self, strs):
        if not strs:return ""
        length, count = len(strs[0]), len(strs)
        for i in range(length): # 第一个单词的长度，遍历第一个单词
            c = strs[0][i] # 第一个单词的每一个字母

            # if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
            for j in range(1,count): # 遍历每一个单词
                # 当前单词第i位与第一个单词第i位不同；
                # 或者，已经遍历完成当前单词j
                # if strs[j][i] != c or i==len(strs[j]):
                ## 想想 or  and 连接判断语句的语法
                if i == len(strs[j]) or strs[j][i] != c: ### 【注意】or的前后顺序不可以颠倒
                    return strs[0][:i]
        return strs[0]


    # 利用python zip特性做
    def longestCommonPrefix_zip(self, strs):
        res = ""
        for word in zip(*strs):
            # print(word)
            word_set = set(word)
            # print(word_set)
            if len(word_set) == 1:
                res += word[0]
            else:
                break
        return res

"""
('f', 'f', 'f')
('l', 'l', 'l')
('o', 'o', 'i')
('w', 'w', 'g')
"""

if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    print(Solution().longestCommonPrefix(strs))