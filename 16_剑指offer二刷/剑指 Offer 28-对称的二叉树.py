"""
easy 二叉树
2021-07-15
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        # 如果是空树，则是对称二叉树
        if not root:return True
        return self.dfs(root.left, root.right)

    def dfs(self, p, q):
        # 如果有一边为空，则返回结果
        if not p or not q:
            return not p and not q
        if p.val != q.val: return False
        return self.dfs(p.left, q.right) and self.dfs(p.right, q.left)


if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(2)
    d = TreeNode(3)
    e = TreeNode(4)
    f = TreeNode(4)
    g = TreeNode(3)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = g
    c.left = f
    print(Solution().isSymmetric(a))

"""
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def recur(L, R):
            if not L and not R: return True
            if not L or not R or L.val != R.val: return False
            return recur(L.left, R.right) and recur(L.right, R.left)

        return recur(root.left, root.right) if root else True
"""