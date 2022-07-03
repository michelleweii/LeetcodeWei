"""
easy 2021-11-08 前序遍历
https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/tu-jie-er-cha-shu-de-si-chong-bian-li-by-z1m/
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.res = []

    def preorderTraversal(self, root: TreeNode):
        if not root:return []
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root: return
        self.res.append(root.val)
        self.helper(root.left)
        self.helper(root.right)

    # 迭代
    def preorder(self, root):
        if not root:return []
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val) # 根节点加入结果中
                if node.right: # 右子树入栈
                    stack.append(node.right)
                if node.left: # 左子树入栈
                    stack.append(node.left)
        return res


if __name__ == '__main__':
    pass