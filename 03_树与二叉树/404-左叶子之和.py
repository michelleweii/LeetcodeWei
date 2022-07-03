"""
easy 2021-12-27 层次遍历ac
# 重点：如何判断是左叶子而不是左节点？
判断当前节点是不是左叶子是无法判断的，必须要通过节点的父节点来判断其左孩子是不是左叶子。
如果该节点的左节点不为空，该节点的左节点的左节点为空，该节点的左节点的右节点为空，则找到了一个左叶子
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 递归
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:return 0

        curvalue = 0
        # 找到左叶子
        if root.left and not root.left.left and  not root.left.right:
            curvalue = root.left.val

        leftvalue = self.sumOfLeftLeaves(root.left)  # 当前节点左子树的左叶子之和
        rightvalue = self.sumOfLeftLeaves(root.right)  # 当前节点右子树的左叶子之和

        sum = curvalue+leftvalue+rightvalue
        return sum

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
    print(Solution().sumOfLeftLeaves(a))
