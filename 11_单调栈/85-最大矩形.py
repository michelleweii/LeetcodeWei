"""
hard 2021-10-26【二维单调递增栈】
1.一行行遍历
2.每行使用题84柱状图中最大的矩形方法计算
3.最后取最大值
"""
class Solution:
    def maximalRectangle(self, matrix):
        n = len(matrix) # n行
        if not n:return 0
        m = len(matrix[0]) # m列
        if n==1 and m==1:return int(matrix[0][0])
        heights = [0 for _ in range(m)]
        # 将每行看做一个新的底，构建新的柱状图，有多少行，就有多少个柱状图
        res = 0
        for i in range(n):
            for j in range(m):
                # 以每行i为底座，一直想上累加（向上延伸）
                if matrix[i][j]=='1':heights[j]+=1
                else: heights[j] = 0
            res = max(res, self.helper(heights))
        return res

    # 维护单调递增栈
    def helper(self, heights):
        heights = [0]+heights+[0]  # 插入两个哨兵
        stk = []
        ans = 0
        for i in range(len(heights)):
            while stk and heights[i]<heights[stk[-1]]:
                h = heights[stk[-1]]
                stk.pop()
                left = stk[-1]
                w = i-left-1 # i是h为最矮柱的右边界
                ans = max(ans, w*h) # 以h为最矮柱的最大面积
            stk.append(i)
        return ans

if __name__ == '__main__':
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    print(Solution().maximalRectangle(matrix))