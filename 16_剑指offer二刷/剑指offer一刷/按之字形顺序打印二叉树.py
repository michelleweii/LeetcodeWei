# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        rs = []
        flag = 1
        if not pRoot: return rs
        queue = []
        queue.append(pRoot)
        while queue:
            cur_level,size = [],len(queue)
            for i in range(size):
                tmp = queue.pop(0)
                cur_level.append(tmp.val)
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
            rs.append(cur_level[::flag])
            flag*=-1

        return rs









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
    print(Solution().Print(a))