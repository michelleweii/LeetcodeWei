"""
middle 2021-12-29
https://www.programmercarl.com/0669.%E4%BF%AE%E5%89%AA%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.html#%E9%80%92%E5%BD%92%E6%B3%95
题目：剔除不在[left,right]区间的值，维护BST性质。
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 确认递归函数参数以及返回值：返回更新后剪枝后的当前root节点
    def trimBST(self, root, low: int, high: int):# -> Optional[TreeNode]:
        if not root:return None

        # 如果root（当前节点）的元素小于low的数值，那么应该递归右子树，并返回右子树符合条件的头结点。
        if root.val<low:
            right = self.trimBST(root.right, low, high)
            return right
        if root.val>high:
            # 寻找符合区间[low, high]的节点
            left = self.trimBST(root.left, low, high)
            return left

        root.left = self.trimBST(root.left, low, high) # root->left接入符合条件的左孩子
        root.right = self.trimBST(root.right, low, high) # root->right接入符合条件的右孩子
        return root

if __name__ == '__main__':
    pass