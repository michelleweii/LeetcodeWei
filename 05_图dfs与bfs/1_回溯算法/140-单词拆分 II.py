"""
hard 2021-12-07 dfs回溯
题目要求（返回所有这些可能的句子）所有可能，那么要用到dfs
https://www.bilibili.com/video/BV1Wq4y1N75f?p=1&share_medium=iphone&share_plat=ios&share_session_id=6432D740-BBBC-4E04-B5ED-AA16ACCA29F3&share_source=WEIXIN&share_tag=s_i&timestamp=1638852961&unique_k=t5O3aMA
(图例)https://leetcode-cn.com/problems/word-break-ii/solution/shou-hua-tu-jie-dan-ci-chai-fen-ii-cong-di-gui-dao/
"""
# 为什么是回溯呢？
# s = "catsanddog", i++, 一直到i=2之前，都没有单词在dict中存在，s[0:3]在dict中，
# 然后新的s = "sanddog", 重复上述过程，s[0:4]在dict中，
# 然后新的s = "dog", 重复上述过程，s[0:2]在dict中，
# 构成一组解，加入进解集中。
# 开始回溯，回溯"sanddog", ..., 回溯到最上上上层，
# 回溯到s = "catsanddog"，i=3时， s[0:4]="cats"在dict中，继续。。。

# 思路：
# 1、如果s中有字符不在worddict中，返回空；（剪枝）
# 2、worddict转为hashmap，因为每次都要判断切分出的单词是否在worddict中；
# 3、开始记忆化递归，记忆化递归的核心在于：我们可以用 map 或数组存储计算结果，数组索引为指针位置，值为子调用的结果。
# 下次遇到相同的子问题时，直接返回 memo 中的缓存值，而不是落入重复的递归。
class Solution:
    def __init__(self):
        self.res = []

    def wordBreak(self, s: str, wordDict): # List[str]) -> List[str]:
        count = {}
        for word in wordDict:
            for c in word:
                count[c] = count.get(c,0) + 1
        # print(count)
        for c in s:
            if count.get(c,0)==0:return self.res
        self.wordDict = wordDict
        # 开始回溯
        self.dfs(s,0,[])
        return self.res

    def dfs(self, s, index, cur_path): # cur_path本次递归的结果子集
        n  = len(s)
        # 定义出口
        if index==n:
            self.res.append(' '.join(cur_path))
            return

        for i in range(index, n):
             # 判断当前substr是否在worddict中
            if s[index: i+1] in self.wordDict:
                # before_add = len(cur_path) # 如果是第一个，没有空格
                cur_path.append(s[index: i+1])
                self.dfs(s, i+1, cur_path)
                cur_path.pop() # 回溯

    """
    # 记忆化递归版本，上述【如果s中有字符不在worddict中，返回空；（剪枝）】过滤了bad case
    def __init__(self):
        self.res = []
        self.memo = {}  # 数组索引为指针位置，值为子调用的结果

    def wordBreak(self, s: str, wordDict): # List[str]) -> List[str]:
        self.wordDict = wordDict
        # 开始回溯
        self.dfs(s,0,[])
        return self.res

    def dfs(self, s, index, cur_path):
        # index本次递归s的起始位置
        # cur_path本次递归的结果子集
        n  = len(s)
        # 定义出口
        if index == n:
            self.res.append(' '.join(cur_path))
            return
            
        # 加入memo中，避免重复计算
        if self.memo.get(s[index:n], 0) != 0:
            return self.memo.get(s[index:n])

        for i in range(index, n):
             # 判断当前substr是否在worddict中
            if s[index: i+1] in self.wordDict:
                # before_add = len(cur_path) # 如果是第一个，没有空格
                cur_path.append(s[index: i+1])
                
                self.memo[i] = s[index: i+1] # 加入memo中，避免重复计算
                
                self.dfs(s, i+1, cur_path)
                cur_path.pop() # 回溯
    """

if __name__ == '__main__':
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    # [
    #   "cats and dog",
    #   "cat sand dog"
    # ]

    # s = "pineapplepenapple"
    # wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    print(Solution().wordBreak(s, wordDict))
