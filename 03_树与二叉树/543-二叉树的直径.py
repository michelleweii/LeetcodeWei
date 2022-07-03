"""
easy 2021-12-12 直径=左子树高度+右子树高度
 最大直径是左子树和右子树的最大深度之和，但是万一最大直径没有经过根节点呢？
 所以说对于树中的每一个结点，都要把它视为根节点，然后比较所有结点的左子树和右子树的最大深度之和，
 取其中的最大值。## 求路径
https://leetcode-cn.com/problems/diameter-of-binary-tree/solution/hot-100-9er-cha-shu-de-zhi-jing-python3-di-gui-ye-/
相关题lc104.二叉树的最大深度
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.res = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:return 0
        self.depth(root)
        return self.res

    def depth(self, root):
        # 先考虑最下层的空节点
        if not root:return 0
        # 考虑中间层的左边的深度以及右节点的深度
        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)
        # 每个结点都要去判断左子树 + 右子树的高度是否大于self.max，更新最大值
        # 上层的深度更新
        self.res = max(self.res, left_depth+right_depth) # 求边的数量
        # 返回给更上一层的深度
        return max(left_depth, right_depth)+1 # 求左右子树高度，求节点的数量


if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    a.right = c
    a.left = b
    b.right = e
    b.left = d
    print(Solution().diameterOfBinaryTree(a))
