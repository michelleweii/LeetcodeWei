"""
middle 2021-12-29 递归遍历（必会）
https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/236-er-cha-shu-de-zui-jin-gong-gong-zu-xian-hou-xu/
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root is None: return None
        # root为p或者root为q，说明找到了p和q其中一个
        if (root is p) or (root is q): return root
        # 递归调用当前节点的左子树
        left = self.lowestCommonAncestor(root.left,p,q)
        # 递归调用当前节点的右子树
        right = self.lowestCommonAncestor(root.right,p,q)
        # 若左子树找到了p，右子树找到了q，说明此时的root就是公共祖先
        if left and right: return root
        # 若左子树是none,右子树不是，说明右子树找到了A或B
        if not left: return right
        # # 若右子树是none,左子树不是，说明左子树找到了A或B
        if not right:return left

if __name__ == '__main__':
    a = TreeNode(3)
    b = TreeNode(5)
    c = TreeNode(6)
    d = TreeNode(2)
    e = TreeNode(7)
    f = TreeNode(4)
    g = TreeNode(1)
    h = TreeNode(0)
    i = TreeNode(8)

    a.right = g
    a.left = b
    b.left = c
    b.right = d
    d.left = e
    d.right = f
    g.right = i
    g.left = h

    p = TreeNode(5)
    q = TreeNode(1)
    print(Solution().lowestCommonAncestor(a,p,q))