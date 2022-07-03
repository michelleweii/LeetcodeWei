# i从1循环至字符串长度的一半，所有字符串长度能整除的i即代表所有可能的子字符串长度；
# 判断子字符串延长给定倍数后是否等于原字符串；

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1,len(s)//2+1):
            if len(s)%i == 0:
                if s[:i]*(len(s)//i) == s:
                    return True

        return False


def main():
    s = "ababab"
    myResult = Solution()
    print(myResult.repeatedSubstringPattern(s))

if __name__ == '__main__':
    main()

    # # 字典:
    # # s = "ababba"
    # if len(s)==1:
    #     return False
    # dict = {}
    # for i in s:
    #     if i not in dict.keys():
    #         dict[i] = 1
    #     else:
    #         count = dict[i]
    #         count += 1
    #         dict[i] = count
    # print(dict) # {'a': 3, 'b': 3}
    # print(dict.keys()) # dict_keys(['a', 'b'])
    # print(dict.items()) # dict_items([('a', 3), ('b', 3)])
    # print(dict.values()) # dict_values([3, 3])
    # tmp = list(dict.values())
    # print(tmp) # [3, 3]