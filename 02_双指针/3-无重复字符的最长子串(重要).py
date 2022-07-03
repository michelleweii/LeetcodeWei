"""
middle 2021-09-26 同向双指针 字节衍生题lc395
与LC209/ LC438/ 类比
思路：
定义两个指针i,j。表示当前扫描到的子串是[i,j]，
扫描过程中维护一个哈希表，表示[i,j]中每个字符出现的次数。
1、指针j向后移动一位，同时将哈希表s[j]的计数+1，hash[s[j]]++；
2、假设j移动前的区间[i,j]中没有重复字符，则 j 移动后，只有s[j]可能出现2次。<重点>
因此我们不断向后移动i，直至区间[i,j]中s[j]的个数等于1为止；
"""
class Solution(object):
    # 2021/05/30
    # 以s[j]为右端点，向左延生，最远能延生到的i的位置
    def lengthOfLongestSubstring(self, s):
        hash_map = {}
        i = 0
        res = 0
        for j in range(len(s)):
            hash_map[s[j]] = hash_map.get(s[j],0)+1
            while hash_map[s[j]]>1:
                hash_map[s[i]] = hash_map[s[i]]-1
                i += 1 # i是最左的有边界
            res = max(res,j-i+1)
        return res

    ## 【扩展】如果允许重复一次字符呢——微软-苏州-Lead面
    # https://www.lintcode.com/problem/928/solution/18275
    def lengthOfLongestSubstringTwoDistinct(self, s):
        if not s: return 0
        n = len(s)
        counter = {} # 多维护了一个hashmap
        longest, left = 0, 0
        for right in range(n):
            counter[s[right]] = counter.get(s[right], 0) + 1
            print('counter',counter)
            while left < right and len(counter) > 2:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            longest = max(longest, right - left + 1)

        return longest

if __name__ == '__main__':
    s = "abcabc"
    print(Solution().lengthOfLongestSubstring(s))
    print(Solution().lengthOfLongestSubstringTwoDistinct(s))