"""
middle
位运算
"""
# 找到list中最长的单词，然后其余元素和它进行比较，如果都有元素相同，找下一个最长的单词
# lines.sort(key=lambda x: len(x))

"""
判断两个字符串中是否有相同元素
find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，
则检查是否包含在指定范围内，如果指定范围内如果包含指定索引值，返回的是索引值在字符串中的起始位置。
如果不包含索引值，返回-1。
str1 = "Runoob example....wow!!!"
str2 = "exam";

print (str1.find(str2))  #7
-----------------------------------------------------------------------------------
info = 'abca'
print(info.find('a'))      # 从下标0开始，查找在字符串里第一个出现的子串，返回结果：0
0
print(info.find('a', 1))   # 从下标1开始，查找在字符串里第一个出现的子串：返回结果3
3
print(info.find('3'))      # 查找不到返回-1
-1

"""
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        maxlen = 0
        words = sorted(words,key=len,reverse=True) # 记！
        # print(words)
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if len(words[i])*len(words[j])>maxlen:
                    # 如果没有相同的元素
                    # for char in words[j]:
                    #     if char not in words[i]:
                    #         print(char)
                    if not any(char in words[i] for char in words[j]):
                        maxlen = max(maxlen,len(words[i])*len(words[j]))
                        # break
        return maxlen


def main():
    words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
    myResult = Solution()
    print(myResult.maxProduct(words))

if __name__ == '__main__':
    main()