import collections
"""
判断字符串集合是否相等
sorted()字典序排序，排完一样了。 o(nlogn)
统计字母出现的个数 o(n)
"""
class Solution(object):
    def groupAnagramsmine(self, strs):
        hash_map = {}
        # 将所有的字符串归类
        for s in strs:
            # keys = ''.join((lambda x:(x.sort(),x)[1])(list(s))) # 将字符串内部按照字典序排序
            keys = ''.join(sorted(s))
            if keys not in hash_map:
                hash_map[keys] = [s]
            else:
                hash_map[keys].append(s)
        # print(hash_map) # {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}
        return list(hash_map.values())

    def groupAnagrams(self, strs):
        groups = collections.defaultdict(list)
        print(list(groups))
        for s in strs:
            groups[tuple(sorted(s))].append(s)
        return list(map(sorted, groups.values()))

if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    myResult = Solution()
    # 第一个字符串的排列之一是第二个字符串的子串
    print(myResult.groupAnagrams(strs))
    # print(myResult.groupAnagramsmine(strs))