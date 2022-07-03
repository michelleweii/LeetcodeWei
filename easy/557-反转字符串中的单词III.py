# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
# 输入: "Let's take LeetCode contest"
# 输出: "s'teL ekat edoCteeL tsetnoc"
# -*- coding:utf-8 -*-
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        # print(s.split())
        for val in s.split():
            result.append(val[::-1])  # 字符串反转
        return (' '.join(result))


def main():
    s = "Let's take LeetCode contest"
    # print(s)
    myresult = Solution()
    print(myresult.reverseWords(s))

if __name__ == "__main__":
    main()
