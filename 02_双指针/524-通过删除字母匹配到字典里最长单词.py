"""
middle 2022-01-04 同向双指针+贪心
https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/solution/gong-shui-san-xie-xiang-jie-pai-xu-shuan-qi20/
# 题目要求：dict中字符串的字符必须要含在s里。字典顺序最小，划重点。
等价于 dict中筛选出是s的子序列（不是子序列的可以直接过），在所有子序列中挑选长度最长，字典序最小的
# 思路：
1. 使用两个指针 i 和 j 分别代表检查到 s 和 dictionary[x] 中的哪位字符；
2. 当 s[i] != dictionary[x][j]，我们使 i 指针右移，直到找到 s 中第一位与 dictionary[x][j] 对得上的位置，
然后当 i 和 j 同时右移，匹配下一个字符；
3. 重复步骤2，直到整个 dictionary[x] 被匹配完。

证明：对于某个字符 dictionary[x][j] 而言，选择 s 中 当前 所能选择的下标最小的位置进行匹配，对于后续所能进行选择方案，
会严格覆盖不是选择下标最小的位置，因此结果不会变差。
"""
# 令 n 为 s 的长度，m 为 dictionary 的长度
# 整体复杂度为 O(mlogm+m∗n)
class Solution:
    def findLongestWord(self, s, dictionary):
        ## 用好python内置函数sort()、find(),比双指针效率更高
        ## 可以用元组表示多关键字排序，第一关键字是长度降序，第二关键字是字符串本身字典序
        dictionary.sort(key=lambda x: (-len(x), x))
        # print(dictionary) # ['a', 'b', 'c']
        n = len(s)
        for x in dictionary:
            m = len(x)
            si, dj = 0, 0
            while si<n and dj<m:
                if s[si] == x[dj]: # 如果字符相等，j就在单词里移动
                    dj += 1
                si += 1 # 指针指向s的一直移动
            # 判断j是否走完
            if dj == m: # 考虑s=aaa,d=aaa的情况
                return x
        return ""

if __name__ == '__main__':
    # s = "abpcplea"
    # dictionary = ["a", "c", "b"]
    s = "aaa"
    dictionary = ["aaa", "aa", "a"]
    print(Solution().findLongestWord(s, dictionary))