"""
hard 2021-12-13 DFS回溯
返回所有可能的结果——DFS
括号题：lc20、lc22
思路：递归遍历划掉)右括号
【图+判断有效括号】https://leetcode-cn.com/problems/remove-invalid-parentheses/solution/gong-shui-san-xie-jiang-gua-hao-de-shi-f-asu8/
【解题视频】https://www.bilibili.com/video/BV15f4y137c5?from=search&seid=9116545148168630233&spm_id_from=333.337.0.0
1、计算删除括号数,lr左括号，rr右括号。
2、回溯，当lr==rr==0，s就有可能是有效括号。
3、判断s是否有效，例如)(，lc20判断是否是有效的括号（其实和LC20不一样）。
"""
class Solution:
    def __init__(self):
        self.res = []

    def removeInvalidParentheses(self, s): #str) -> List[str]:
        # 1、计算要移除的左右括号数
        left_remove, right_remove = 0, 0
        for ch in s:
            left_remove += (ch=='(')
            if left_remove==0:
                right_remove += (ch==')')
            else: # left_remove>0,与右括号抵消
                left_remove -= (ch==')')
        self.back_trace(0, left_remove, right_remove, s)
        # ()())(), 需要移出的右括号有1个，需要移出的左括号0个
        return self.res

    # 2、回溯，移出括号
    # 这算是什么问题呢
    def back_trace(self, start_index, left_remove, right_remove, s):
        # 完成条件
        if left_remove==0 and right_remove==0 and self.is_valid(s):
            self.res.append(s)
        # for s
        # 离开条件
        # 做出选择
        # 回溯
        # 撤销选择
        for i in range(start_index, len(s)):
            if i>start_index and s[i]==s[i-1]: continue # 剪枝
            if s[i]=='(' and left_remove > 0:
                # 出了下面的函数，s没有变，所以自动回溯
                # 因此传入函数的s少了index=i, 所以start_index不用+1，因为传入i相当于自动+1
                # 举例，s=abcd,i=1,s[i]=b, s[:i]+s[i+1:]=acd,i=1,s[1]=c
                self.back_trace(i, left_remove-1, right_remove, s[:i]+s[i+1:])
                # s[:i]+s[i+1:]自动回溯
            if s[i] == ')' and right_remove > 0:
                self.back_trace(i, left_remove, right_remove-1, s[:i] + s[i + 1:])

    # 3、判断是否是有效的括号
    # 前置知识：统计左括号、右括号数量是否平衡;
    # 在任意一个时刻，右括号数量一定是<=左括号数量的,如果>说明左边至少一个右括号无法匹配
    # count')'<=count'(', i<n-1
    # count')'==count'(', i=n-1
    def is_valid(self, s):
        count = 0
        for ch in s:
            if ch =='(': count+=1  # 相当于左括号先入栈
            elif ch ==')': count-=1 # 遇到右括号，左括号弹栈
            if count<0:return False
        return count==0


if __name__ == '__main__':
    s = "(a)())()" #lr=0, rr=1, 多了一个右括号
    print(Solution().removeInvalidParentheses(s))