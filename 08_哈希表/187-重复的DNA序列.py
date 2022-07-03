"""
middle 2021-10-27
找出出现次数多于1的 & 长度为10的子串
思路：
1、从前向后扫描，当子串出现第二次时，记录在答案中；时间复杂度O(N)
时间复杂度：O(NL) 因为每次用字符串做哈希表的hash key都要花 O(L)的时间复杂度，所以整体是 O(NL)
空间复杂度：O(N)
视频link：https://www.bilibili.com/video/BV1Lb411w74Y?spm_id_from=333.999.0.0  00:25
"""
class Solution: # 92.64%
    def findRepeatedDnaSequences(self, s):
        if not s:return []
        hashmap = {}
        res = []
        # print(len(s))
        for i in range(len(s)-10+1): # 注意是-9
            tmp = s[i:i+10]
            # print(i, tmp)
            hashmap[tmp] = hashmap.get(tmp,0)+1
            if hashmap.get(tmp,0)==2:
                res.append(tmp)
        return res

if __name__ == '__main__':
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    # s = "AAAAAAAAAAA"
    print(Solution().findRepeatedDnaSequences(s))