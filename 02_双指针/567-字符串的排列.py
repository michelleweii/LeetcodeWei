"""
middle 2022-01-04 同向双指针|滑动窗口
（与567字符串的排列+76最小覆盖子串+438找到字符串中所有字母异位词相似）
https://leetcode-cn.com/problems/permutation-in-string/solution/zi-fu-chuan-de-pai-lie-hua-dong-chuang-k-sos8/
思路：
flag：记录窗口中满足条件的字符个数
若一个字符进入窗口，应该增加 window 计数器；若一个字符将移出窗口，应该减少 window 计数器；
当 flag 满足 tMap 时应收缩窗口；收缩窗口的时候应该更新最终结果。
当发现某个字符在 window 中的数量满足了 tMap 的需要，就要更新 flag，表示有一个字符已满足要求。
当 right - left + 1 == t.length()时，窗口大小 "等于" 字符串 t 的长度时移动 left 缩小窗口，
因为各种排列的长度显然应该是一样的。
-----------------------------------------------------------------------------------
# 窗口中可以有其他字符，但是 windowMap 中只存放当前窗口中与要找的字符串 t 中字符相等字符的出现次数
# S = "EBBANCF"，当窗口下标为 [0, 5] 时，windowMap = {A:1, B:2, C:1}
# T = "ABC"，其中 tMap = {A:1, B:1, C:1}
"""
from collections import Counter
class Solution:
    # 同LC76模板
    # s1是短的， s2是长的
    def checkInclusion(self, s1, s2):
        len1,len2 =len(s1),len(s2)
        # window 记录窗口中的字符；tMap 记录需要凑齐的字符(need)
        curmap = {}
        needmap = Counter(s1)

        right, left = 0, 0
        flag = 0 # 记录窗口中满足条件的字符个数

        while right < len2:
            # 如果当前字符在t_map中
            if s2[right] in needmap:
                # 就将该字符加入到window中，只记录在tmap中的字符
                curmap[s2[right]] = curmap.get(s2[right],0)+1
                # 如果这个字符和t_map中一样了，说明有一个字符满足要求了
                if curmap.get(s2[right],0) == needmap.get(s2[right],0):
                    flag += 1
            # 寻找最优解
            # 窗口大小 "等于" 字符串 t 的长度时移动 left 缩小窗口
            while right-left+1 == len1:
                # 收缩窗口的时候更新最终结果
                if flag==len(needmap): return True

                # 字符移除窗口
                if s2[left] in needmap:
                    # 移出left时，如果是tmap中的元素，flag--
                    if curmap.get(s2[left],0) == needmap.get(s2[left],0):
                        flag -= 1
                    # 当前窗口移除元素
                    curmap[s2[left]] = curmap.get(s2[left],0)-1
                # 缩小窗口
                left += 1
            # 扩大窗口
            right += 1
        return False

    def check_ori(self,s1,s2):
        lens1, lens2 = len(s1), len(s2)
        if not s1 or not s2 or lens1 > lens2: return False

        needmap = Counter(s1)
        need_cnt = len(needmap) # 有多少个字母需要满足, {字母:字母个数}
        windowmap = {}

        i = 0
        for j in range(lens2):
            if s2[j] in needmap:
                windowmap[s2[j]] = windowmap.get(s2[j], 0) + 1 # 当前窗口只记录需要的字符
                if needmap.get(s2[j],0)==windowmap.get(s2[j],0): # 有一个字符满足条件了
                    need_cnt-=1

            # 寻找最优解
            while j-i+1 == lens1:
                if need_cnt == 0: return True

                # 【这里】破坏窗口性质
                if s2[i] in needmap:
                    if windowmap.get(s2[i],0)==needmap.get(s2[i],0):
                        need_cnt+=1
                    windowmap[s2[i]] = windowmap.get(s2[i],0)-1
                i+=1

        return False

if __name__ == '__main__':
    # s1 = "ab"
    # s2 = "eidbaooo"
    s1 = "ABC"
    s2 = "EBBACF"
    myResult = Solution()
    # 第一个字符串的排列之一是第二个字符串的子串
    print(myResult.checkInclusion(s1, s2))