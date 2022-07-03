"""
middle 栈
2021-07-15
动图更容易理解
https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/solution/mian-shi-ti-31-zhan-de-ya-ru-dan-chu-xu-lie-mo-n-2/
"""
class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        stk = []
        i = 0 # 标记popped顺序
        for x in pushed:
            stk.append(x)
            while stk and stk[-1]==popped[i]:
                stk.pop()
                i += 1
        return not stk

if __name__ == '__main__':
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 3, 5, 1, 2]
    print(Solution().validateStackSequences(pushed, popped))
