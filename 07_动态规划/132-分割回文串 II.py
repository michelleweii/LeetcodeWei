"""
hard 2021-12-06 一维dp
本题做法：https://leetcode-cn.com/problems/distinct-subsequences/solution/shou-hua-tu-jie-xiang-jie-liang-chong-ji-4r2y/
一般做法：https://www.bilibili.com/video/BV1NJ411v7k9?from=search&seid=14432392895864513820&spm_id_from=333.337.0.0
一般做法：(python)https://leetcode-cn.com/problems/palindrome-partitioning-ii/solution/132-fen-ge-hui-wen-chuan-iidong-tai-gui-3hqva/
"""
# 【扩展】回文子串基础题5、647
# 题目：对s进行分割，分割出的结果都要是回文串，求最少分割次数
# 状态定义：dp[i] 为以下标为 i 的字符作为结尾（结尾）的最小分割次数（答案）；
# 回文串定义：vaild[i][j] = 1 if s[i:j+1] s串中i-j位置是回文串，else 0
# 先枚举右端点dp[l][r], 以r为结尾的s子串，再枚举左端点找到分割点

# 长度为n的字符串，最多切n-1刀

"""
为了方便，我们约定所有下标从 1 开始。
即对于长度为 n 的字符串，我们使用 [1,n] 进行表示。
这样做的目的是为了减少边界情况判断，这本身也是对于「哨兵」思想的运用。
"""

class Solution:
    def minCut(self, s: str) -> int:
        if not s:return 0
        n = len(s)
        # 定义回文,先用一个二维数组来保存整个字符串的回文情况
        is_valid = [[False]*n for _ in range(n)]
        # 保存回文串，注意这里的遍历顺序，见lc647
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i<=1 or is_valid[i+1][j-1]):
                    is_valid[i][j] = True

        # 定义dp, dp[i] = min cuts of s[0-i]
        dp = [n for _ in range(n)] # 定义一个无穷大的值，只要取不到的值就行 dp=[sys.maxsize]*len(s)
        # 遍历, 以i为结尾的字符串，的最小回文分割数
        for i in range(n):
            # 边界，如果s[0:i]是回文串，只要切0刀，所以dp[i]=0
            if is_valid[0][i]:
                dp[i] = 0
                continue
            else:
                # 开始枚举j，找到最优的分割点
                for j in range(0,i):
                    if is_valid[j+1][i]: # 因为dp[j]先计算得到
                        # 先遍历的i，本题是要找到最少分割次数，所以遍历j的时候要取最小的dp[i]。
                        dp[i] = min(dp[i], dp[j]+1) # 注意这里不是要 dp[j] + 1 和 dp[i]去比较，而是要在遍历j的过程中取最小的dp[i]！

        return dp[n-1]


if __name__ == '__main__':
    s = "ab"
    print(Solution().minCut(s))