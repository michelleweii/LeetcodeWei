"""
hard 2022-01-20 2维DP(度小满面试题20190513)
状态定义：dp[i][j] 代表 word1 中前 i 个字符，变换到 word2 中前 j 个字符，最短需要操作的次数。
https://leetcode-cn.com/problems/edit-distance/solution/zi-di-xiang-shang-he-zi-ding-xiang-xia-by-powcai-3/
https://leetcode-cn.com/problems/edit-distance/solution/edit-distance-by-ikaruga/（感觉这个更清晰）
1）word1[i] == word2[j]，dp[i][j] = dp[i-1][j-1]
2）word1[i] != word2[j]，dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
dp[i-1][j-1] 表示替换操作
dp[i-1][j] 表示删除操作。dp[i-1][j]是删除了word1。
dp[i][j-1] 表示插入操作。dp[i][j-1]是删除了word2。
# 为什么要这样表示的原因？
因为题意要求从word1到word2，word1是可变的，word2是不可变的。
dp[i-1][j] 表示当前word1[i]与word2[j]是不匹配的，那我去找下word1[i-1]与word2[j]匹配的情况，
如果该情况下最小，那就删除当前的word1[i]。dp[i][j-1]表示我去看看word1[i]与word2[j-1]的匹配情况，如果匹配的结果是最小的，那就增加一个word1[i+1] == word2[j]就行了。
"""
class Solution:
    # 自底向上
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        # print(dp) # [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
        # 状态定义：dp[i][j] 代表 word1 中前 i 个字符，变换到 word2 中前 j 个字符，最短需要操作的次数。
        # 初始化第一行、第一列
        # 需要考虑 word1 或 word2 一个字母都没有，即全增加/删除的情况，所以预留 dp[0][j] 和 dp[i][0]
        for i in range(n+1):
            dp[0][i] = i # word1是空的，只能增加
        for j in range(m+1):
            dp[j][0] = j # word2是空的，只能删除
        # print(dp) # [[0, 1, 2, 3, 4, 5], [1, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 0]]

        for i in range(1, m+1): # word1的个数
            for j in range(1, n+1): # word2的个数
                if word1[i-1] == word2[j-1]: # 注意dp[i]的下标是index=i-1
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        return dp[m][n]

# 对“dp[i-1][j-1] 表示替换操作，dp[i-1][j] 表示删除操作，dp[i][j-1] 表示插入操作。”的补充理解：
# 以 word1 为 "horse"，word2 为 "ros"，且 dp[5][3] 为例，即要将 word1的前 5 个字符转换为 word2的前 3 个字符，也就是将 horse 转换为 ros，
# 因此有：
# (1) dp[i-1][j-1]，即先将 word1 的前 4 个字符 hors 转换为 word2 的前 2 个字符 ro，然后将第五个字符 word1[4]（因为下标基数以 0 开始）
# 由 e 替换为 s（即替换为 word2 的第三个字符，word2[2]）；
# (2) dp[i][j-1]，即先将 word1 的前 5 个字符 horse 转换为 word2 的前 2 个字符 ro，然后在末尾补充一个 s，即插入操作；
# (3) dp[i-1][j]，即先将 word1 的前 4 个字符 hors 转换为 word2 的前 3 个字符 ros，然后删除 word1 的第 5 个字符。
if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    print(Solution().minDistance(word1, word2))
