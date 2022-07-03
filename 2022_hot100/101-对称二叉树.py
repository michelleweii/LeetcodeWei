"""
easy 2021-12-26 递归遍历
没到叶子节点就继续向下递归
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        if not root: return True
        return self.check(root.left, root.right)

    def check(self, root1, root2):
        # 到叶子了
        if not root1 and not root2: return True
        elif not root1 and root2: return False
        elif not root2 and root1: return False
        elif root1.val != root2.val: return False
        return self.check(root1.left, root2.right) and self.check(root1.right, root2.left)

    def isSymmetric_old(self, root):
        def check(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return check(node1.left, node2.right) and check(node1.right, node2.left)
        return check(root, root)

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
