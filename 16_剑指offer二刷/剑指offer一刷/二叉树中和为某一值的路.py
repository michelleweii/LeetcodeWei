# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        res = []
        path = []
        if not root:return res
        self.dfs(root,expectNumber,path,res)
        return res


    def dfs(self,root,sum,path,res):
        # print(sum)
        # if not root: return
        path.append(root.val)
        sum -= root.val
        if not root.left and not root.right and sum==0:
            # print(path)
            res.append(path[:])
        if root.left:
            self.dfs(root.left,sum,path,res)
        if root.right:
            self.dfs(root.right,sum,path,res)
        path.pop()

if __name__ == '__main__':
    a = TreeNode(5)
    b = TreeNode(4)
    c = TreeNode(8)
    d = TreeNode(11)
    e = TreeNode(13)
    f = TreeNode(4)
    g = TreeNode(7)
    h = TreeNode(2)
    i = TreeNode(5)
    j = TreeNode(1)
    a.right = c
    a.left = b
    b.left = d
    d.left = g
    d.right = h
    c.right = f
    c.left = e
    f.right = j
    f.left = i
    sum = 22
    print(Solution().FindPath(a,sum))