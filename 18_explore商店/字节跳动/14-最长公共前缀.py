"""
easy 2022-02-25 纵向遍历
# python zip特性
"""
class Solution:
    # 纵向遍历
    def longestCommonPrefix(self, strs):
        if not strs:return ""

        lens1, size = len(strs[0]), len(strs)
        # 先遍历第一个单词
        for i in range(lens1):
            for j in range(1, size):
                print([0][i], strs[j])
                if i==len(strs[j]) or strs[0][i]!=strs[j][i]:
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