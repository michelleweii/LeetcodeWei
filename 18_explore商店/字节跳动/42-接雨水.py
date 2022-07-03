
# 2022-02-27
# 单调（递减）栈
class Solution:
    def trap(self, height) -> int:
        if not height:return 0
        stk = []
        res = 0
        for i in range(len(height)):

            while stk and height[stk[-1]]<height[i]:
                # 弹栈
                right = height[i]
                cur = height[stk[-1]]
                stk.pop()
                if stk:
                    left = height[stk[-1]]
                    h = min(left,right)-cur
                    w = i-stk[-1]-1
                    res += w*h
                    # print('res',w*h)
            stk.append(i)

        return res


if __name__ == '__main__':
    height = [4, 2, 0, 3, 2, 5] # 9
    print(Solution().trap(height))