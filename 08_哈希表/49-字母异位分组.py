"""
middle 2022-03-14 哈希
使用sorted对字符串排序，sorted(strs)
https://leetcode-cn.com/problems/group-anagrams/solution/kan-ping-lun-qu-zhi-qian-sha-ye-bu-hui-k-0os9/
思路：
1.将不同的字符串转换为字符数组并按照字母顺序进行排序
2.异位词排序后的结果相同，故可以作为哈希表的key值
3.将字母异位词组成的集合作为哈希表的value值
"""
#         d = dict()
#         for i in range(len(strs)):
#             word = ''.join(sorted(strs[i]))
#             if word not in d:
#                 d[word] = [strs[i]]
#             else:
#                 d[word].append(strs[i])
#         return list(d.values())
class Solution:
    def groupAnagrams(self, strs):
        if not strs or len(strs)==1:return [strs]
        hashmap={}
        for s in strs:
            chars = [x for x in s] # 将字符串转化为字符数组
            chars.sort() # 对字符数组按照字母顺序排序
            key = ''.join(chars)
            if key not in hashmap:
                hashmap[key] = [s]
            else:
                hashmap[key].append(s) # 【attention:这里直接append】
        return list(hashmap.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # 输出: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    print(Solution().groupAnagrams(strs))