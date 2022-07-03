"""
middle bi-tree+2_dfs-递归
2021-07-13
"""
"""
python做法
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        idx = inorder.index(root.val)
        root.left = self.buildTree(preorder[1: idx + 1], inorder[0: idx])
        root.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1: ])
        return root
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.hash_map = {}

    def buildTree(self, preorder, inorder):
        self.preorder = preorder
        self.inorder = inorder
        # 快速在中序遍历中，找到某个值的下标
        for i, val in enumerate(inorder):
            self.hash_map[val] = i
        return self.dfs(0, len(preorder)-1, 0, len(inorder)-1)

    # 去2个序列中分别找左子树node，右子树node
    def dfs(self, pl, pr, il, ir):
        if pl>pr:return None # dfs一定要有循环的出口
        root = TreeNode(self.preorder[pl])
        k = self.hash_map[self.preorder[pl]]
        # 去前序遍历中找左子树，去中序遍历中找左子树
        root.left = self.dfs(pl+1, pl+k-il, il, k-1)
        # 去前序遍历中找右子树，去中序遍历中找右子树
        root.right = self.dfs(pl+k-il+1, pr, k+1, ir)
        return root

if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    print(Solution().buildTree(preorder, inorder))