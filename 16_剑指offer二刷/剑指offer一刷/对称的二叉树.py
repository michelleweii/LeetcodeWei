# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot:return True
        return self.helper(pRoot.left,pRoot.right)
    def helper(self,p,q):
        if not p or not q:return not p and not q
        # 只有两棵树都是空的才是空
        if p.val != q.val:return False
        return self.helper(p.left,q.right) and self.helper(p.right,q.left)


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
    print(Solution().isSymmetrical(a))