"""
middle 同向双指针
2021-07-19
"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s: return 0
        hashmap = {}
        i = 0
        res = -1
        for j in range(len(s)):
            # if s[j] not in hashmap:
            hashmap[s[j]]= hashmap.get(s[j],0)+1
            while i<j and hashmap[s[j]]>1:
                hashmap[s[i]] = hashmap.get(s[i],0)-1
                i += 1
            # print(i, j)
            res = max(res, j-i+1)
        return res


if __name__ == '__main__':
    # s = "pwwkew"
    # s = "abcabcbb"
    s  = ""
    print(Solution().lengthOfLongestSubstring(s))