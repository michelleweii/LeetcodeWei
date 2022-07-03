# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        self.pre = pre
        self.tin = tin
        self.hashmap = {}
        for idx,node in enumerate(tin):
            self.hashmap[node]=idx
        # print(hashmap)
        return self.dfs(0,len(pre)-1,0,len(tin)-1)

    def dfs(self,pl,pr,il,ir):
        if pl>pr:return None
        root = TreeNode(self.pre[pl])
        k = self.hashmap[root.val]
        # 寻找左子树，在前序遍历找，在中序遍历找
        left = self.dfs(pl+1,k-il+pl,il,k-1)
        right = self.dfs(k-il+pl+1,pr,k+1,ir)
        root.left = left
        root.right = right
        return root


if __name__ == '__main__':
    pre = [1,2,4,7,3,5,6,8]
    tin = [4,7,2,1,5,3,8,6]
    print(Solution().reConstructBinaryTree(pre,tin))