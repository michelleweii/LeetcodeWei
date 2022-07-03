"""
middle 2021-06-21 反向双指针
https://leetcode-cn.com/problems/sum-of-square-numbers/solution/shuang-zhi-zhen-de-ben-zhi-er-wei-ju-zhe-ebn3/
# 左指针low = 0，右指针high = sqrt(c)
"""
class Solution:
    def judgeSquareSum(self, c):
        left, right = 0, int(c**0.5)
        # print(left, right, c**0.5) # 0 2 2.23606797749979
        while left <= right: # 注意这里是<=，因为c = 4返回ture
            sums = right*right+left*left
            if sums > c:right -= 1
            elif sums < c: left+=1
            else: return True
        return False

if __name__ == '__main__':
    # c = 5 # 1*1+2*2
    c = 2 # 1*1+1*1
    # 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a^2 + b^2 = c
    ans = Solution()
    print(ans.judgeSquareSum(c))