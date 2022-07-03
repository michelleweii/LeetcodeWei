"""
hard 2021-11-09 区间DP
区间动态规划：区间长度大的状态值可以由区间长度小的状态值递推而来
https://leetcode-cn.com/problems/scramble-string/solution/miao-dong-de-qu-jian-xing-dpsi-lu-by-sha-yu-la-jia/
定义：dp[i][j][len] 表示从字符串 S 中 i 开始长度为 len 的字符串是否能变换为从字符串 T 中 j 开始长度为 len 的字符串，
所以答案是 dp[0][0][n]

代码优化：https://leetcode-cn.com/problems/scramble-string/solution/gong-shui-san-xie-yi-ti-san-jie-di-gui-j-hybk/
"""
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        lens1 = len(s1)
        lens2 = len(s2)
        if lens1!=lens2:return False
        # 初始化dp3维数组dp[i][j][k]
        # i为0~lens1-1共lens1个， j为0~lens1-1共lens1个， k为1~lens1+1共lens1个
        # k是字符串长度（当前想要测试的范围）
        dp = [ [ [False]*(lens1+1) for _ in range(lens1) ] for _ in range(lens1)]
        # 初始化单个字符的情况
        for i in range(lens1):
            for j in range(lens1):
                dp[i][j][1] = s1[i]==s2[j]
        # 前面排除了s1和s2为单个字符的情况，那么我们就要划分区间了，
        # k从2到lens1，也就是划分为s1[:k]和s1[k:]
        # 枚举区间长度 2～lens1
        for k in range(2, lens1+1):
            # 枚举 S 中的起点位置 for (int i = 0; i <= lens1 - k; i++) {
            # 也就是在s1中枚举i的位置，因为后面会出现i+w的情况，而w最大就是k，
            # 就会有i+k的情况，所以i的取值范围就是0~lens1-k
            for i in range(lens1-k+1):
                # 枚举 T 中的起点位置 for (int j = 0; j <= lens1 - k; j++) {
                for j in range(lens1-k+1):
                    # 枚举划分位置，s1[:k]中从
                    # 要从哪个index=w开始划分, 分成S1,S2
                    for w in range(1, k): #
                        # 第一种情况：S1->T1,S2->T2
                        if dp[i][j][w] and dp[i+w][j+w][k-w]:
                            dp[i][j][k] = True
                            break
                        # 第二种情况：S1->T2,S2->T1
                        # S1起点: i，T2起点: j+(前面那段长度k-w)，
                        # S2起点:(i+前面长度k)
                        if dp[i][j+k-w][w] and dp[i+w][j][k-w]:
                            dp[i][j][k] = True
                            break

        return dp[0][0][lens1]

if __name__ == '__main__':
    # s1 = "great"
    # s2 = "rgeat" # True
    s1 = "abcde"
    s2 = "caebd" # False
    print(Solution().isScramble(s1,s2))