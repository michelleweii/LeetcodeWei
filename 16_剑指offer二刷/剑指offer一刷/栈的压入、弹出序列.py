# -*- coding:utf-8 -*-
class Solution:
    """
    先将第一个放入栈中，这里是1，然后判断栈顶元素是不是出栈顺序的第一个元素，
    这里是4，很显然1≠4，所以我们继续压栈，直到相等以后开始出栈，出栈一个元素，
    则将出栈顺序向后移动一位，直到不相等，这样循环等压栈顺序遍历完成，
    如果辅助栈还不为空，说明弹出序列不是该栈的弹出顺序。
    """
    def IsPopOrder(self, pushV, popV):
        if not pushV:return False
        stk = [] # 声明一个辅助栈
        for item in pushV:
            stk.append(item)
            while stk and stk[-1]==popV[0]:
                # 当辅助栈的栈顶元素和出栈元素相同时，
                # 两个一起弹出
                stk.pop()
                popV.pop(0)
        if stk:
            return False
        return True


if __name__ == '__main__':
    pushV = [1,2,3,4,5]
    popV = [4,5,3,2,1]
    print(Solution().IsPopOrder(pushV,popV))
