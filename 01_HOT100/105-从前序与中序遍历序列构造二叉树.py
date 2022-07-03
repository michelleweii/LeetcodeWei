"""
middle 2021-12-10 二叉树构造
从前序与中序遍历序列构造二叉树

# 树里面return None是啥含义？就是空节点
# 猜测：叶子节点下的就是None
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.hashmap = {}

    def buildTree(self, preorder, inorder):
        # 中序结果hash，方便定位node所在下标，用于分割左右子树
        for i in range(len(inorder)):
            self.hashmap[inorder[i]] = i

        self.preorder = preorder
        self.inorder = inorder

        return self.dfs(0, len(preorder)-1, 0, len(inorder)-1)

    def dfs(self, pl, pr, il, ir):
        """
        :param pl: param pr: 前序遍历起始、结束位置
        :param il: param ir: 中序遍历起始、结束位置
        """
        # 定义出口
        if pl>pr:
            return None
        # 遍历节点，开始递归
        root = TreeNode(self.preorder[pl])
        k = self.hashmap[self.preorder[pl]]
        # k-il 中序遍历中，左子树的长度
        # ir-k 中序遍历中，右子树的长度
        # 得到 pl+k-il 前序遍历中，左子树的长度
        # 不断找左子树、找右子树
        root.left = self.dfs(pl+1, pl+k-il, il, k-1)
        root.right = self.dfs(pl+k-il+1, pr, k+1, ir)
        return root


if __name__ == '__main__':
    pass