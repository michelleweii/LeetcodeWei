"""
middle 2021-12-14 bst
题目：返回bst第k小元素, ac myself
空间复杂度：O(h)，h为二叉树高度。
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root, k):
        self.count = k
        self.res = 0
        self.inorder(root)
        return self.res

    def inorder(self, root):
        if root.left and self.count>0: self.inorder(root.left)
        self.count -= 1

        if self.count == 0:
            self.res = root.val

        if root.right and self.count>0:self.inorder(root.right)

if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    c.left = a
    c.right = d
    a.right = b

    k = 1
    print(Solution().kthSmallest(c,k))