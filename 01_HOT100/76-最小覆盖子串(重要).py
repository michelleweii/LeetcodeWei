"""
hard 2021-06-10 同向双指针
（与567字符串的排列+76最小覆盖子串+438找到字符串中所有字母异位词相似）
子串是连续的；T可能包含重复字符（下面连接的图例有助于理解）
https://leetcode-cn.com/problems/minimum-window-substring/solution/tong-su-qie-xiang-xi-de-miao-shu-hua-dong-chuang-k/
如何判断S的子串包含了T中的所有字符？
- 分别统计s的子串和T中每个字符出现的次数，逐个对比（哈希表）。
- S中每个字符出现的次数>=T中该字符出现的次数(s的哈希表里可以包括t中不存在的key,字符出现的顺序不重要)

我们用一个字典need来表示当前滑动窗口中需要的各元素的数量，一开始滑动窗口为空，用T中各元素来初始化这个need，
当滑动窗口扩展或者收缩的时候，去维护这个need字典，例如当滑动窗口包含某个元素，我们就让need中这个元素的数量减1，代表所需元素减少了1个；
当滑动窗口移除某个元素，就让need中这个元素的数量加1。
记住一点：need始终记录着当前滑动窗口下，我们还需要的元素数量，我们在改变i,j时，需同步维护need。
"""
# 1\left右移，是可行解到最优解的过程
# 2\right先移动，找到问题的可行解
# 3\hash[key]>0 说明需要key，<0说明该key是多余的.
# 所有元素的数量都<=0时，表示当前滑动窗口不再需要任何元素
from collections import Counter
# sW_count, tW_count = Counter(sW), Counter(tW) # 统计字符串里每个字符的个数
# need[] == 0，说明这个字符正好
# need[]<0，说明这个字符多余了
class Solution:
    def minWindow(self, s, t):
        ls = len(s)
        lt = len(t)
        if not s or not t or ls < lt:
            return ''

        # # 最小覆盖子串长度
        res = ls + 1 # 初始赋值为一个不可能达到的数
        left, right = 0, 0

        # 对t中的字符计数
        # need = {}
        # for c in t:
        #     need[c] = need.get(c, 0)+1
        need = Counter(t) # 当前滑动窗口中需要的各元素的数量
        need_cnt = len(t) # 所需元素的总数量,=3则为还差3个元素(还需要几个元素可以成为t)
        start = 0 # start是最小覆盖串开始的index

        # [left, right) # 一开始l,r都是0，带入[)中，[0,0)这个区间是空的
        # 右指针向右扩展，遍历s，长的那个字符串
        while right < ls:
            # s[right] 右指针看见的元素
            # 先后顺序不能变化 比如aa
            if need[s[right]] > 0: # 如果需要这个元素
                need_cnt -= 1
            need[s[right]] -= 1 # 把右边的字符加入窗口，不需要的就{R:-1}即可

            # 寻找最优解
            if need_cnt == 0: # 步骤一：滑动窗口包含了所有T元素
                while (left<right and need[s[left]]<0):  # 步骤二：增加left，排除多余元素，<0说明是多余元素
                    need[s[left]] += 1
                    left += 1 # 指针右移
                # 出while循环的时候，left位于不能再右移的位置

                if (right-left+1<res):
                    res = right-left+1 # 最小覆盖子串长度
                    start = left # 再从这个位置开始向右扩展

                #【这里】破坏窗口性质，寻找下一个最优解
                # left向右移动后窗口肯定不能满足了，重新开始循环
                # left是要前进一位的，开始寻找下一个满足条件的滑动窗口
                need[s[left]] += 1 # 该元素移出了，则还需要该元素
                left += 1
                need_cnt += 1

            right += 1

        return '' if res > ls else s[start:start+res]
"""
暴力解法
- 枚举输入字符串s的所有长度>=t的子串；
- 逐个判断这些子串中，哪些子串覆盖了字符串t的所有字符；
- 在枚举的过程中，记录符合条件的，长度最短的那个子串。
"""
if __name__ == '__main__':
    S = "ADOBECODEBANC" # "ab" #
    T = "ABC" # "a" #
    # BANC
    print(Solution().minWindow(S, T))
