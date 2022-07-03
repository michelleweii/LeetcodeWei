"""
easy
哈希表
# 字符串中str.count(i),计算单个字母出现的次数

"""
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        for i in range(len(t)):
            if t[i] not in s:
                return False
        return True
# return sorted(s)==sorted(t)

if __name__ == '__main__':
    s = "aacc"
    t = "ccac"

    myResult = Solution()
    print(myResult.isAnagram(s, t))