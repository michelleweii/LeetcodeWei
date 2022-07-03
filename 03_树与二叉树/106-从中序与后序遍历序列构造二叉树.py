"""
middle 2021-11-12 二叉树构造
根据一棵树的中序遍历与后序遍历构造二叉树。
具体分析看lc 105

中序遍历的顺序通过k很好划分
难点在后序遍历的划分，边界考虑
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.hashmap = {} # 在中序遍历中快速找到根节点下标，便于分割进一步划分左右子树，进行递归

    def buildTree(self, inorder, postorder):
        self.inorder = inorder
        self.postorder = postorder
        for i in range(len(inorder)):
            self.hashmap[inorder[i]] = i
        return self.dfs(0, len(inorder)-1, 0, len(postorder)-1)

    def dfs(self, pl, pr, tl, tr):
        # 定义出口
        if pl>pr:return None # 返回空节点
        root = TreeNode(self.postorder[tr])
        k = self.hashmap[self.postorder[tr]]
        # 通过中序遍历，得到分割后左子树长度：k-pl
        # 分割后右子树长度：pr-k
        # 得到在后序遍历中的左子树区间：[tl, tl+k-pl]
        # 【error】右子树区间：[tr-pr-k, tr-1] # 从后面往前推会错误，原因：
        # 右子树区间正向推：tl+左子树长度+1
        root.left = self.dfs(pl, k-1, tl, tl+k-pl-1)
        root.right = self.dfs(k+1, pr, tl+k-pl, tr-1)
        return root

if __name__ == '__main__':
    pass
