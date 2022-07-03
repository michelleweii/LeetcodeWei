"""
easy 2021-12-13 栈 【经典题】
"""
class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        # 如果length为奇数，可以直接返回false
        if n%2==1:return False
        stk = []
        for i in range(n):
            if stk and s[i]==')' and s[stk[-1]]=='(':
                # print(1)
                stk.pop()
                continue
            elif stk and s[i]==']' and s[stk[-1]]=='[':
                stk.pop()
                continue
            elif stk and s[i]=='}' and s[stk[-1]]=='{':
                stk.pop()
                continue
            stk.append(i)

        if stk: # 如果栈不空
            return False
        return True

if __name__ == '__main__':
    s = "()[]{}"
    print(Solution().isValid(s))