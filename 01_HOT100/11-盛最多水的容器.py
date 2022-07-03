"""
middle 2021-12-30 双指针反向 O(N)
（动图很棒）https://leetcode-cn.com/problems/container-with-most-water/solution/container-with-most-water-shuang-zhi-zhen-fa-yi-do/
我的思考：
使用双指针的原因是根据这个问题的特点，【存水的高度取决于两边较短的那个内壁的高度】。
为什么这道题不用单调栈？
"""
# 无论是移动短板或者长板，我们都只关注移动后的新短板会不会变长，
# 而每次移动的木板都只有三种情况，比原短板短，比原短板长，与原短板相等；
# 如向内移动长板，对于新的木板：（为什么不移动长板的原因？）
# 1.比原短板短，则新短板更短。2.与原短板相等或者比原短板长，则新短板不变。所以，向内移动长板，一定不能使新短板变长。

# 【重点】
# 在每个状态下，无论长板或短板向中间收窄一格，都会导致水槽 底边宽度 -1 变短：
#
# 若向内 移动短板 ，水槽的短板 min(h[i], h[j]) 可能变大，因此下个水槽的面积 可能增大 。
# 若向内 移动长板 ，水槽的短板 min(h[i], h[j]) 不变或变小，因此下个水槽的面积 一定变小 。
class Solution:
    def maxArea(self, height):
        i, j = 0, len(height)-1
        res = 0
        while i<j:
            # 注意，这里每次移动的都是短板！！！
            if height[i]<height[j]:
                res = max(res, height[i]*(j-i))
                i+=1
            else:
                res = max(res, height[j]*(j-i))
                j-=1
        return res


if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(height))