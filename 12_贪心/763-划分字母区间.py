"""
middle 2021-12-22 贪心
(看图理解) https://programmercarl.com/0763.%E5%88%92%E5%88%86%E5%AD%97%E6%AF%8D%E5%8C%BA%E9%97%B4.html#%E6%80%9D%E8%B7%AF
题目：把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中
思路：在遍历的过程中相当于是要找每一个字母的边界，如果找到之前遍历过的所有字母的最远边界，说明这个边界就是分割点了。
此时前面出现过所有字母，最远也就到这个边界了。
1、统计每一个字符最后出现的位置
2、从头遍历字符，并更新字符的最远出现下标，如果找到字符最远出现位置下标和当前下标相等了，则找到了分割点
"""
class Solution:
    def partitionLabels(self, s: str):# -> List[int]:
        # 1\hashmap中存每个字符的最远位置
        # hashmap = [0] * 26 # i为字符，hash[i]为字符出现的最后位置
        # for i in range(len(s)):
        #     # print(ord(s[i]), ord('a'), i) # 97 97 0
        #     hashmap[ord(s[i]) - ord('a')] = i # 2\统计每一个字符最后出现的位置
        # # print(hashmap) # [8, 5, 7, 14, 15, 11, 13, 19, 22, 23, 20, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # 可以用以下来代替
        hashmap = {ch: index for index, ch in enumerate(s)} # #存储某个字母对应地最后一个序号
        result = []
        left = 0 # 定位每次区间的左端点
        right = 0  # 定位每次区间的右端点
        # print(hashmap)
        for i in range(len(s)):
            # print(i, right, hashmap[ord(s[i])-ord('a')])
            # right = max(right, hashmap[ord(s[i])-ord('a')]) # 3\找到字符出现的最远边界
            right = max(right, hashmap[s[i]])
            if i==right:
                result.append(right-left+1)
                left = i+1
        return result

if __name__ == '__main__':
    # s = "a"
    s = "ababcbacadefegdehijhklij" #[9,7,8]
    print(Solution().partitionLabels(s))