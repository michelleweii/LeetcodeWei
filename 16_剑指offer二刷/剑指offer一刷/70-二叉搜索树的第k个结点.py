# -*- coding:utf-8 -*-
# 完全不记得怎么做
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 中序遍历时相减
class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.cnt = 0
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot: return None
        node = self.KthNode(pRoot.left,k)
        if node:
            return node
        self.cnt+=1
        # print(self.cnt)
        if self.cnt==k:
            return pRoot
        node = self.KthNode(pRoot.right,k)
        if node:
            return node

"""
#     self.res = []
#     if not pRoot:return None
#     self.inorder(pRoot,k)
#     return self.res.pop() if self.res else None
#
# def inorder(self,root,k):
#     if not root:return
#     self.inorder(root.left,k)
#     k -= 1
#     print(root.val,k)
#     if k == 0:
#         return self.res.append(root)
#     if k>0:self.inorder(root.right,k)
"""




if __name__ == '__main__':
    a = TreeNode(2)
    b = TreeNode(1)
    c = TreeNode(3)
    # d = TreeNode(3)
    # e = TreeNode(6)
    a.right = c
    a.left = b
    print(Solution().KthNode(a,3))