"""
middle 2022-05-30 类似dfs遍历的模拟
https://leetcode.cn/problems/spiral-matrix-ii/solution/luo-xuan-ju-zhen-ii-by-leetcode-solution-f7fp/
https://www.acwing.com/solution/content/15338/ 扩散方向
[这个扩散方向可以学习]https://leetcode.cn/problems/spiral-matrix-ii/solution/luo-xuan-ju-zhen-ii-mo-ni-jie-fa-dai-ma-pu5ar/
【核心】检验下一个位置是否合法, 不合法则更新方向, 并重新计算下一个位置
坐标轴
x<---
    |
    y
"""
class Solution:
    # 模板解法
    def generateMatrix(self, n: int):# -> List[List[int]]:
        x,y,d=0,0,0
        matrix=[[0]*n for _ in range(n)]
        dx=[-1,0,1,0]
        dy=[0,1,0,-1]
        # dx=[0, 1, 0, -1]
        # dy=[1, 0, -1, 0]

        for i in range(n*n):
            # print(i+1,x,y)
            matrix[x][y]=i+1
            a=x+dx[d]
            b=y+dy[d]
            if a<0 or a==n or b<0 or b==n or matrix[a][b]>0:
                d=(d+1)%4
                a=x+dx[d]
                b=y+dy[d]

            x=a
            y=b
        return matrix

if __name__ == '__main__':
    # martix = [
    #          [ 1, 2, 3 ],
    #          [ 4, 5, 6 ],
    #          [ 7, 8, 9 ]
    #         ]
    n=3
    print(Solution().generateMatrix(n))