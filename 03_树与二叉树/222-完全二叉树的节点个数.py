"""
middle 2021-12-27 递归遍历
# 层次遍历记录节点变量++
# 后序遍历，与LC104二叉树深度类似
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:return 0
        # 当前节点左子树个数
        leftnum = self.countNodes(root.left)
        # 当前节点右子树个数
        rightnum = self.countNodes(root.right)
        treenum = leftnum+rightnum+1 # 加上自己
        return treenum

if __name__ == '__main__':
    pass