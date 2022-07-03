"""
middle 2022-01-04 同向双指针|滑动窗口+数组哈希表（与567，76相似）
LC3.无重复字符的最长子串
（与567字符串的排列+76最小覆盖子串+438找到字符串中所有字母异位词相似）
https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/solution/438-zhao-dao-zi-fu-chuan-zhong-suo-you-z-nx6b/
---------------------------------
解题思路
（1）初始化 left = right = 0 把索引 <左闭右闭> 区间 [left, right] 当做一个 "窗口"。
（2）不断增加 right 指针扩大窗口 [left, right]，直到窗口中的字符串符长度与字符串 t 的长度相等。
（3）此时，停止增加 right，转而不断增加 left 指针缩小窗口 [left, right]，直到窗口中的字符串长度不再符合要求。
    同时，每增加一次 left，就要更新一轮结果。
（4）重复第 2 和第 3 步，直到 right 到达字符串 s 的尽头。
其中，第 2 步相当于在寻找一个 "可行解"，第 3 步相当于在判断这个可能的 "可行解"，最终找到 "最优解"。
"""
class Solution(object):
    # 套用模板解法
    def findAnagrams(self, s, p):
        from collections import Counter
        res = []
        n, m = len(s), len(p)
        if n<m:return res

        window_map = {} # window 记录窗口中的字符
        p_map = Counter(p) # Counter({'a': 2})
        left, right = 0, 0

        while right < n: # 遍历长的字符串
            window_map[s[right]] = window_map.get(s[right], 0) + 1
            # 通过窗口左边界的右移left++，把所有多余的字符移出去
            while window_map.get(s[right], 0) > p_map.get(s[right], 0): # 与L3不同，这里是与map做比较
                window_map[s[left]] = window_map.get(s[left], 0) - 1 # 类似LC3，重复的只可能是right新入的
                left += 1
            # print(window_map)
            if right-left+1 == m:
                res.append(left)
            right += 1 # 扩充右边界
        return res

    def findAnagrams2(self, s: str, p: str):# -> List[int]:
        n, m, res = len(s), len(p), []
        if n < m: return res
        p_cnt = [0] * 26
        s_cnt = [0] * 26

        for i in range(m):
            p_cnt[ord(p[i]) - ord('a')] += 1
        # print('p_cnt', p_cnt) # 字母a是两个
        left = 0
        for right in range(n):
            cur_right = ord(s[right]) - ord('a')
            s_cnt[cur_right] += 1
            while s_cnt[cur_right] > p_cnt[cur_right]:
                cur_left = ord(s[left]) - ord('a')
                s_cnt[cur_left] -= 1
                left += 1
            if right - left + 1 == m:
                res.append(left)
        return res


if __name__ == '__main__':
    # s = "baa"
    # p = "aa"
    s="cbae"
    p="abc"
    myResult = Solution()
    print(myResult.findAnagrams(s, p))
    # print(myResult.findAnagrams2(s, p))