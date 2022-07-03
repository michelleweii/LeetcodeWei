"""
middle 2021-11-08 树回溯
https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/solution/129-qiu-gen-jie-dian-dao-xie-jie-dian-sh-j11c/
标准的回溯模板（同112、113）：https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/solution/biao-zhun-de-hui-su-mo-ban-by-jiubukaiji-t0a2/
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root):
        if not root:return 0
        self.res,self.path = [],[]  # path把每一条路径保存下来
        self.backtrace(root)
        return sum(self.res)

    # 标准回溯
    def backtrace(self, root):
        if not root: return
        self.path.append(root.val)  # 因为都是从根出发的，所以第一个root.val不用pop
        # 到叶子节点啦
        if not root.left and not root.right:
            print(self.path)
            tmp = self.get_sum(self.path)
            self.res.append(tmp)
        if root.left:
            self.backtrace(root.left)
            self.path.pop()
        if root.right:
            self.backtrace(root.right)
            self.path.pop()

    def get_sum(self, nums):
        s = 0
        for x in nums:
            s = s*10+x
        return s

# class Solution:
    #     def sumNumbers(self, root: TreeNode) -> int:
    #         if not root:return 0
    #         self.res,self.path = [],[]  # path把每一条路径保存下来
    #         self.path.append(root.val)
    #         self.backtrace(root)
    #         return sum(self.res)
    #
    #     # 标准回溯
    #     def backtrace(self, root):
    #         if not root: return
    #         # self.path.append(root.val)  # 因为都是从根出发的，所以第一个root.val不用pop
    #         # 到叶子节点啦
    #         if not root.left and not root.right:
    #             # print(self.path)
    #             tmp = self.get_sum(self.path)
    #             self.res.append(tmp)
    #         if root.left:
    #             self.path.append(root.left.val)
    #             self.backtrace(root.left)
    #             self.path.pop()
    #         if root.right:
    #             self.path.append(root.right.val)
    #             self.backtrace(root.right)
    #             self.path.pop()
## ------------------------------------------------------------------------------------------------------------------
    def sumNumbers_plus(self, root: TreeNode) -> int:
        self.res = 0
        if not root:return 0
        self.helper(root, 0)
        return self.res

    # root是当前遍历的节点，number是从根节点到当前节点路径表示的数。
    # 递归回溯
    def helper(self, root, number):
        if not root:return 0
        number = number*10 + root.val
        # 遍历到叶节点时，将根节点到当前叶节点路径维护的数字加入答案中。
        if not root.left and not root.right: # 叶子节点
            self.res += number
        if root.left: self.helper(root.left, number)
        if root.right: self.helper(root.right, number)
## ------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.left = b
    a.right = c
    print(Solution().sumNumbers(a))