"""
hard 2021-12-12 区间DP（快手）
dp[i][j]表示气球区间i-j之间的最优结果,最大金币数。
https://leetcode-cn.com/problems/burst-balloons/solution/yi-wen-tuan-mie-qu-jian-dp-by-bnrzzvnepe-2k7b/
"""
# 在区间(i,j)中，找到划分点k，得到(选)dp[i][k]+nums[k]+dp[k][j]，(不选)dp[i][j]
class Solution:
    def maxCoins(self, nums):# List[int]) -> int:
        # nums.insert(0,1)
        # nums.insert(len(nums),1)
        nums = [1]+nums+[1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        # 1\对每一个区间长度进行循环
        # # 长度从3开始，n从2开始;
        # # 开区间长度会从3一直到len(nums);
        for lens in range(2, n): # 区间长度
            print('lens', lens, n-lens)
            # # 2\对于每一个区间长度，循环区间开头的i
            for i in range(0, n-lens): # 以 i 为 开头
                # print(i, n, lens, n-lens) # 0 6 2 4
                j = i+lens # # 以 j 为 终点
                # 3\计算这个区间的最多金币
                # k是(i,j)区间内最后一个被戳的气球
                for k in range(i+1, j):  # k取值在(i,j)开区间中, # 以 k 为分割点，进行分治
                    # 以下都是开区间(i,k), (k,j)
                    dp[i][j] = max(dp[i][k]+nums[i]*nums[k]*nums[j]+dp[k][j], \
                                   dp[i][j])

        return dp[0][-1] #dp[0][n-1]


if __name__ == '__main__':
    nums = [3, 1, 5, 8]
    print(Solution().maxCoins(nums))