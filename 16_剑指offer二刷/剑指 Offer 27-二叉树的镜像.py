"""
easy 二叉树
交换二叉树的左右子树
2021-07-15
# https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/solution/mian-shi-ti-27-er-cha-shu-de-jing-xiang-di-gui-fu-/
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 递归
    def mirrorTree(self, root):
        if not root: return root
        root.right = self.mirrorTree(root.right)
        root.left = self.mirrorTree(root.left)
        root.right, root.left = root.left, root.right
        return root

    # 遍历
    def mirrorTree2(self, root: TreeNode) -> TreeNode:
        if not root: return root
        queue = [root]
        while queue:
            node = queue.pop()
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
            node.left, node.right = node.right, node.left
        return root


def print_tree(root):
    res = []
    queue = []
    queue.append(root)
    while queue:
        tmp = queue.pop(0)
        res.append(tmp.val)
        if tmp.left:
            queue.append(tmp.left)
        if tmp.right:
            queue.append(tmp.right)
    print(res)

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
    print(print_tree(a))
    res = Solution().mirrorTree(a)
    print(print_tree(res))