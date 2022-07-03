"""
easy 2021-11-08 后序遍历
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
    def postorderTraversal(self, root: TreeNode):# -> List[int]:
        if not root:return self.res
        self.post_order(root)
        return self.res
    def post_order(self,root):
        if not root:return
        self.post_order(root.left)
        self.post_order(root.right)
        self.res.append(root.val)

    # 迭代

if __name__ == '__main__':
    pass
