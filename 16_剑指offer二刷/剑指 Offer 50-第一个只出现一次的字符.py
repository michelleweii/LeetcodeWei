"""
easy hashmap
2021-07-18
"""
# c in dic 为判断字典中是否含有键 c
# not c in dic 整体为一个布尔值
# https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/solution/mian-shi-ti-50-di-yi-ge-zhi-chu-xian-yi-ci-de-zi-3/
class Solution:
    def firstUniqChar(self, s: str):
        hashmap = {}
        for x in s:
            hashmap[x] = True if x not in hashmap else False
        for x in s:
            if hashmap[x]:return x
        return " "



if __name__ == '__main__':
    s = "abaccdeff" # b
    print(Solution().firstUniqChar(s))