"""
middle 一维dp
2021-07-18
"""
# 状态定义：设动态规划列表 dp ，dp[i] 代表以 nums[x_i+1] 为结尾的数字的翻译方案数量。
# https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/solution/mian-shi-ti-46-ba-shu-zi-fan-yi-cheng-zi-fu-chua-6/
class Solution:
    def translateNum(self, num):
        s = str(num)
        dp = [0 for _ in range(len(s)+1)]
        # print(len(s)) # 5
        # print(len(dp)) # 6
        dp[0] = 1 #
        dp[1] = 1 # 第 1 位数字,nums[0] 的翻译方法数量为 1
        for i in range(2, len(dp)):
            tmp = s[i-2:i]
            if int(tmp)<=25 and int(tmp)>=10:
                dp[i] = dp[i-1]+dp[i-2]
            else:
                dp[i] = dp[i-1]
        print("dp", dp)
        return dp[len(s)]

if __name__ == '__main__':
    num = 12258
    print(Solution().translateNum(num))