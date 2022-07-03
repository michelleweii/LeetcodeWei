"""
hard 2021-12-08 2维DP【倒叙】
https://www.bilibili.com/video/BV1JK4y1t7i4
题目要求：从左上角顺利到达右下角，所需要的最小初始值。顺利：达到某个格子不能为0。
已知：到达右下角，需要状态=1(不能<0，又要最小)
求左上角初始值

思路：
dp[i][j]：从（i，j）出发，到达终点需要最少的血量；
1、到终点格子前至少要有1，那么终点格子为1-(格子值)；要不然根本没命到这里；
2、初始化最后一列、最后一行；由终点格子递推上去；
3、填dp表格
x+value=1, x=1-value, x=new_value-value
x：来这个格子之前的血量
value：该格子的血量
new_value: 落在这个格子的血量，终点new_value=1
"""
class Solution(object):
    def calculateMinimumHP(self, dungeon):#: List[List[int]]) -> int:
        rows = len(dungeon)
        cols = len(dungeon[0])
        dp = [[1]*(cols) for _ in range(rows)]

        dp[rows-1][cols-1] = max(1, 1-dungeon[rows-1][cols-1])
        # 初始化边界值
        """
        为什么与1取max呢？
        因为有些格子求出的x，是负数，因为该格子血量太充裕了，可以让来之前是负数
        但是题目要求，负数就死了啊，所以来这个格子前的x，最小也要是1
        """
        # 最后一行，按行递推
        for j in range(cols-2, -1, -1):
            dp[rows-1][j] = max(1, dp[rows-1][j+1]-dungeon[rows-1][j])
        # 最后一列，按列递推
        for i in range(rows-2, -1, -1):
            dp[i][cols-1] = max(1, dp[i+1][cols-1]-dungeon[i][cols-1])
        # print(dp)
        # 倒叙填表
        for i in range(rows-2, -1, -1):
           for j in range(cols-2, -1, -1):
               # 从右边转化过来 dp[i][j+1]-dungeon[i][j]
               # 从下面转化过来 dp[i+1][j]-dungeon[i][j]
               # 两种转化取min
                dp[i][j] = max(1, min(dp[i][j+1]-dungeon[i][j], dp[i+1][j]-dungeon[i][j]))
        # print(dp)
        return dp[0][0]
"""
总结
这道题的dp是倒序的，这点很重要，为什么不能像【最小路径和】一样是正序的？
因为【最小路径和】是无状态的，你会发现【最小路径和】倒序dp也是可以的，
这道题由于有“加血”的过程，只能依赖后面的值判断需要的血量。
所以这里的dp[i][j]表达的意思是：“从（i，j）出发，到达终点需要最少的血量”。
因此，正序的含义为“从起点出发，到达位置（i，j）所需要的最少血量”；
倒序的含义是“从（i，j）出发，到达终点需要最少的血量”。初始血量本来就是要求的，所以只能倒序dp。
"""


if __name__ == '__main__':
    dungeon = [[-2,-3,3],
                [-5,-10,1],
                [10,30,-5]]
    print(Solution().calculateMinimumHP(dungeon))
    print(float('inf')) # inf