"""
hard 2021-10-26回顾 【单调递增栈】字节
[这个好理解]https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/bao-li-jie-fa-zhan-by-liweiwei1419/
https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/zhao-liang-bian-di-yi-ge-xiao-yu-ta-de-zhi-by-powc/
思路：枚举以每个柱形(栈顶元素)为高度的最大矩形的面积
是以i为中心，向左找第一个小于 heights[i] 的位置 left_i；
向右找第一个小于 heights[i] 的位置 right_i，
即最大面积为 heights[i] * (right_i - left_i -1)

res =（该矩形的高度）*（左右边界的距离）
注意！ 以第i个柱子为矮柱！
"""
class Solution:
    def largestRectangleArea(self, heights):
        heights = [0]+heights+[0]  # 插入两个哨兵
        # print(heights)
        stk = []
        res = 0
        for i in range(len(heights)):
            # 单调递增栈
            # 如果当前i元素小于栈顶元素，说明栈顶元素找到了它右边第一个比它小的元素
            # 在栈顶元素左侧，都是比栈顶元素小的。while一直向前计算，
            # 直到恢复单调递增栈
            while stk and heights[i]<heights[stk[-1]]: # <才是求比栈顶元素右边小的right
                h = heights[stk[-1]]
                stk.pop()
                res = max(res, (i-stk[-1]-1)*h) # 为什么求宽度-1？题目要求是柱子
            stk.append(i)
        return res
    # 以1，5 6 2 为例
    # 此时i在2，栈顶为6，出栈后的新栈顶为5
    # 遍历到2的时候，可以求出以6为矮柱的面积， （2index-5index-1）*6
    # 2<5, 继续求5为挨柱的面积，(2index-1index-1)*5

if __name__ == '__main__':
    heights = [2,1,5,6,2,3]
    # [2, 4]
    myresult = Solution()
    print(myresult.largestRectangleArea(heights))
