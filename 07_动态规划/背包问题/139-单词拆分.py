"""
middle 2021-11-01 dp完全背包
[完全背包+考虑排列顺序]，外层循环为 target ，内层循环为选择池 wordDict。
dp[i] 表示 s 的前 i 位是否可以用wordDict中的单词表示。
- target = s
- arrs = wordDict
边界条件，我们定义 dp[0] = true 表示空串且合法。
"""
# 考虑顺序，外层target，内层arrs。内循环正序。
# https://leetcode-cn.com/problems/coin-change/solution/yi-tao-kuang-jia-jie-jue-bei-bao-wen-ti-h0y40/
class Solution:
    def wordBreak(self, s: str, wordDict):
        # dp[i] 表示 s 的前 i 位是否可以用wordDict中的单词表示。
        dp = [False] * (len(s)+1)
        dp[0] = True

        for i in range(1, len(s)+1): # target
            for word in wordDict: # arrs
                sz = len(word)
                # if i-word_len>=0:print(i, word_len, s[i-word_len: i])
                if i-sz>=0 and s[i-sz: i]==word:  #in wordDict:
                    dp[i] = dp[i] or dp[i-sz]
                    # 不选word dp[i]
                    # 选word dp[i-sz]
        return dp[-1]

if __name__ == '__main__':
    # s = "leetcode"
    # wordDict = ["leet", "code"]
    # s = "catsandog"
    # wordDict = ["cats", "dog", "sand", "and", "cat"]
    # s = "applepenapple"
    # wordDict = ["apple", "pen"]
    s = "dogs"
    wordDict = ["dog", "s", "gs"]
    print(Solution().wordBreak(s, wordDict))

"""
1 1 d
2 1 o
2 2 do
3 3 dog
[True, False, False, True, False]
3 1 g
3 2 og
4 3 ogs
4 1 s
[True, False, False, True, True]
4 2 gs
[True, False, False, True, False]
False
"""