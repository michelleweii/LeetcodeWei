
# 2022-03-01
# 问题：s1 的排列之一是 s2 的 子串，True or False

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lens1, lens2 = len(s1), len(s2)
        if not s1 or not s2 or lens1 > lens2: return False

        needmap = Counter(s1)
        need_cnt = len(needmap) # 有多少个字母需要满足, {字母:字母个数}
        windowmap = {}

        i = 0
        for j in range(lens2):
            if s2[j] in needmap:
                windowmap[s2[j]] = windowmap.get(s2[j], 0) + 1 # 当前窗口只记录需要的字符
                if needmap.get(s2[j],0)==windowmap.get(s2[j],0):
                    need_cnt-=1

            while j - i + 1 == lens1:
                if need_cnt == 0: return True

                if s2[i] in needmap:
                    if windowmap.get(s2[i],0)==needmap.get(s2[i],0):
                        need_cnt+=1
                    windowmap[s2[i]] = windowmap.get(s2[i],0)-1
                i+=1

        return False


if __name__ == '__main__':
    # s1 = "ab"
    # s2 = "eidbaoo"
    # s1 = "ab"
    # s2 = "eidboaoo"
    s1 = "a"
    s2 = "ab"
    print(Solution().checkInclusion(s1,s2))