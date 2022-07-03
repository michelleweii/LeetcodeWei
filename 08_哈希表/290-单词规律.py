# 思路：
# 相同单词是否都映射到了相同字母
# 相同字母是否都映射到了相同单词
class Solution:
    def wordPattern(self, pattern, s):
        ps_hash_map = {}
        sp_hash_map = {}
        words = s.split(' ')
        if(len(words) != len(pattern)):return False

        for i in range(len(words)):
            p = pattern[i]
            w = words[i]

            if not (ps_hash_map.get(p,0)): ps_hash_map[p] = w
            if not (sp_hash_map.get(w,0)): sp_hash_map[w] = p
            if ps_hash_map[p] != w or sp_hash_map[w] != p:
                return False

        return True

if __name__ == '__main__':
    # pattern = "abba"
    # str = "dog cat cat dog"
    pattern = "abba"
    str = "dog dog dog dog"

    print(Solution().wordPattern(pattern,str))