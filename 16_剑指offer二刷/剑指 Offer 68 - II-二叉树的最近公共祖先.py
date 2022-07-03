"""
easy 2021-07-20 二叉树
https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/236-er-cha-shu-de-zui-jin-gong-gong-zu-xian-hou-xu/
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:return root
        if root==p or root==q:return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 当 left 和 right 同时不为空 ：说明 p, q分列在 root的 异侧 （分别在 左 / 右子树），
        # 因此 root 为最近公共祖先，返回 root
        if left and right:return root
        if left:return left
        return right

if __name__ == '__main__':
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    d = TreeNode(15)
    e = TreeNode(7)
    a.right = c
    a.left = b
    c.right = e
    c.left = d
    p = TreeNode(15)
    q = TreeNode(7)
    print(Solution().lowestCommonAncestor(a,p,q))