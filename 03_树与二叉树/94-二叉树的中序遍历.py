"""
easy 2021-12-25 二叉树遍历
https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/
"""
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？栈
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 递归
    def inorderTraversal_recursive(self, root):
        res = []
        self.helper(root,res)
        return res
    def helper(self,root,res):
        if not root:return
        self.helper(root.left,res)
        res.append(root.val)
        self.helper(root.right,res)
    # 迭代
    def inorderTraversal(self, root):
        if not root:return []
        stack, res, cur = [], [], root
        while stack or cur:
            while cur: # cur入栈，并到达最左端的叶子节点
                stack.append(cur)
                cur = cur.left # 左子树不断入栈
            tmp = stack.pop()
            res.append(tmp.val) # 出栈时再加入结果
            cur = tmp.right # 遍历右节点，再将右节点的左子树全部入栈
        return res

if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.right = b
    b.left = c
    print(Solution().inorderTraversal(a))