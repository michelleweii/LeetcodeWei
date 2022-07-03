"""
middle 2022-01-20 dfs回溯
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()
【重点】https://leetcode-cn.com/problems/generate-parentheses/solution/hui-su-suan-fa-by-liweiwei1419/
【Attention】右括号'）'一定要比左括号'（'多。
选）剩余[(()]，怎么都不能满足条件。
https://leetcode-cn.com/problems/generate-parentheses/solution/cpython3java-1dfs-2hui-su-by-hanxin_hanx-690m/
"""
class Solution(object):
    def generateParenthesis(self, n):
        if not n:return []
        self.path, self.res = [], []
        self.backtrace(n, n)
        return self.res

    def backtrace(self, left, right):
        """
        :param left:左括号还有几个可以使用
        :param right:右括号还有几个可以使用
        :return:
        """
        # 在递归终止的时候，直接把它添加到结果集即可，注意与「力扣」第 46 题、第 39 题区分
        if left==0 and right==0:
            self.res.append(''.join(self.path[:]))
            return

        # 右括号'）'一定要比左括号'（'多
        # ）剩余[(()]，怎么都不能满足条件
        if left>right:
            return

        if left>0:
            # 下面3句可以用这1句代替
            # dfs(path + "(", left - 1, right, res);
            self.path.append('(')
            self.backtrace(left-1, right)
            self.path.pop()

        if right>0:
            self.path.append(')')
            self.backtrace(left, right-1)
            self.path.pop()

    # dfs
    # class Solution:
    #     def generateParenthesis(self, n: int) -> List[str]:
    #
    #         def dfs(cur: str, left: int, right: int) -> None:
    #             if left == n and right == n:
    #                 res.append(cur)
    #                 return
    #
    #             if left < n:
    #                 dfs(cur + '(', left + 1, right)
    #             if left > right:
    #                 dfs(cur + ')', left, right + 1)
    #
    #         res = []
    #         dfs('', 0, 0)
    #         return res

if __name__ == '__main__':
    n = 3 # ['((()))', '(()())', '(())()', '()(())', '()()()']
    print(Solution().generateParenthesis(n))