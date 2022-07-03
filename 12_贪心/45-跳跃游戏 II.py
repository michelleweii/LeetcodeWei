"""
middle 2021-12-22 贪心
(lc55的进阶版) https://programmercarl.com/0045.%E8%B7%B3%E8%B7%83%E6%B8%B8%E6%88%8FII.html
https://leetcode-cn.com/problems/jump-game-ii/solution/45-by-ikaruga/
题目：使用最少的跳跃次数到达数组的最后一个位置
分析：本题要计算最小步数，那么就要想清楚什么时候步数才一定要+1呢？
以最小的步数增加覆盖范围，覆盖范围一旦覆盖了终点，得到的就是最小步数。（题目说了一定能跳到终点）
"""
class Solution:
    def jump(self, nums):
        n = len(nums)
        if n<=1: return 0
        jump = 0 # 记录跳跃的次数
        end = 0 # 当前的覆盖最大区域
        max_pos = 0 # 能跳到最远的距离，最大的覆盖区域

        # 对每一次 跳跃 用 for 循环来模拟
        for i in range(n):
            # 跳完一次之后，更新下一次 起跳点 的范围。
            # 在可覆盖区域内更新最大的覆盖区域
            max_pos = max(i+nums[i], max_pos)
            if i==end and end!=n-1: # 已经走到了当前跳跃步数的边界,跳到最后一个位置就结束了
                jump += 1  # 我们不得不再跳一次（重点理解）
                end = max_pos # 并记录当前跳跃步数能到的最远位置
                if max_pos >= n-1: break

        return jump


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4] # 2
    print(Solution().jump(nums))