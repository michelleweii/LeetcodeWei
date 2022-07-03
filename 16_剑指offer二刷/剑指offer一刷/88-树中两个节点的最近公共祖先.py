# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root: return None
        if root==p or root==q: return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left and right: return root
        if left: return left
        return right



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
    print(Solution().lowestCommonAncestor(a, p, q))