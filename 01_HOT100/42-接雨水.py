"""
hard 2021-06-02 【单调递减栈】：stk存储的是index
# https://leetcode-cn.com/problems/trapping-rain-water/solution/trapping-rain-water-by-ikaruga/
思路：注意题目的性质，【当后面的柱子高度比前面的低时，是无法接雨水的】
所以维护单调递减栈，当新入元素比栈顶元素大时，就开始计算面积，栈顶元素出栈；
当新入元素比栈顶元素小时，该元素入栈；(更低的柱子以为这后面如果能找到高柱子，这里就能接到雨水，所以入栈把它保存起来)
- 计算面积要注意：
1、雨水区域的右边 r 指的自然是当前索引 i; 左边 l 就是新的栈顶 st.top()
2、水坑的高度就是左右两边更低的一边减去底部，宽度是在左右中间
"""
class Solution:
    def trap(self, height):
        if len(height) <= 1: return 0
        res, stk = 0, []
        for i in range(len(height)):
            # 当 当前元素比栈顶元素大时(维护非严格单调减)
            # 当找到一根比前面高的柱子，就可以计算接到的雨水
            while stk and height[i]>height[stk[-1]]:
                cur = stk[-1]
                stk.pop() # 删掉栈顶元素index
                # 可以加哨兵解决该问题
                if not stk: break # 必须左边还有，才能计算红色部分的体积
                # left和i取min
                left = stk[-1]
                h = min(height[i],height[left])-height[cur]
                w = i-left-1 # 为什么求宽度-1？题目要求是柱子
                res += h*w
            stk.append(i)
        return res

    # 类似LC11，双指针解法
    # 接雨水最大容量，取决于短板
    # https://leetcode-cn.com/problems/trapping-rain-water/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-w-8/
    # 太难了
    # def two_pointers(self, height):
    #     if len(height)<=1:return 0
    #     i, j = 0, len(height)-1
    #     res = 0
    #     while i<j:
    #         if height[i]<height[j]:# 移动短板height[i]
    #             res = max(res, (j-i-1)*height[i]) # w*h
    #             j-=1
    #         else: # 移动短板height[j]
    #             res = max(res, (j-i-1)*height[i]) # w*h
    #             i+=1
    #     return res

# 2021-10-26
# 2021-12-16
if __name__ == '__main__':
    height = [4,2,0,3,2,5]
    myresult = Solution()
    print(myresult.trap(height))
    # print(myresult.two_pointers(height))