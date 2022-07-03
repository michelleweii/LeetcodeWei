"""
hard 2022-03-21 dp
栈 or dp都可以解决
--------------------------------------
https://leetcode-cn.com/problems/longest-valid-parentheses/solution/dong-tai-gui-hua-si-lu-xiang-jie-c-by-zhanganan042/
状态定义：dp[i] 表示以 i 结尾的最长有效括号
思路分析：
1. 当 s[i] 为 (,dp[i] 必然等于 0，因为不可能组成有效的括号；
2. 那么 s[i] 为 )
    2.1 当 s[i-1] 为 (，那么 dp[i] = dp[i-2] + 2；
    2.2 当 s[i-1] 为 ) 并且 s[i-dp[i-1] - 1] 为 (，那么 dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]；
"""
# ()(()，结果是2，因为答案要求连续
class Solution(object):
    def dpSolution(self,s):
        # dp数组，其中第 i 个元素表示以下标为 i 的字符结尾的最长有效子字符串的长度
        n = len(s)
        if n<2: return 0
        dp = [0] * n # dp[i] 表示以 i 结尾的最长有效括号
        res = 0
        for i in range(n):
            if i>0 and s[i]==')':
                # () 情况
                if s[i-1]=='(':
                    dp[i]=dp[i-2]+2 # 在历史匹配数上+2
                # #)()(())) 情况，就是(())
                # 当前i的对称点索引是否存在
                # 和s[i]配对对位置，并判断其是否是 (即可。和其配对对位置为：i−dp[i−1]−1。
                elif s[i-1]==')' and i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=='(':
                    dp[i]=dp[i-1]+2+dp[i-dp[i-1]-2]
                if dp[i]>res:
                    res=dp[i]
        return res

    # 更容易理解
    def dp(self,s):
        if not s: return 0
        n = len(s)
        dp = [0] * n
        for i in range(n):
            if s[i] == '(': dp[i] = 0  # <---- 虽然已经初始化过
            if s[i] == ')' and i > 0:
                if s[i-1] == '(':
                    if i - 2 >= 0:  # <---- 判断 i - 2
                        dp[i] = dp[i - 2] + 2
                    else:
                        dp[i] = 2
                elif s[i-1] == ')' and s[i - dp[i-1] - 1] == '(' and i - dp[i-1] - 1 >= 0:
                    if i - dp[i-1] - 2 >= 0:   # <---- 判断 i - dp[i-1] - 2
                        dp[i] = dp[i-1] + 2 + dp[i - dp[i-1] - 2]
                    else:
                        dp[i] = dp[i-1] + 2
        return max(dp)

    # # 栈: 存'('的下标
    # 如果是'('就直接入栈；如果是')'就开始匹配；
    # 匹配分情况讨论：
    # 1、如果栈为空，start+=1
    # 2、如果栈顶是'('，栈顶弹栈，# case 1 弹完如果栈为空()()：更新长度 res = max(res, index-start+1)
    #                       # case 2 弹完栈不为空(())：更新长度 res = max(res, index-stk.top())
    def longestValidParentheses(self, s):
        stk = []
        res = 0
        start = 0 # 记录入栈i
        for i in range(len(s)):
            if s[i]=='(': stk.append(i)
            else:
                if stk: # 如果栈不为空
                    stk.pop()
                    # case 1
                    if not stk: res = max(res, i-start+1)
                    # case 2
                    else: res = max(res, i-stk[-1])
                else: # 如果栈是空的，没办法匹配
                    start = i+1 # ")()())()()("
        return res


if __name__ == '__main__':
    # s = "(()"
    s = "()(()"
    # print(Solution().longestValidParentheses(s))
    print(Solution().dpSolution(s))