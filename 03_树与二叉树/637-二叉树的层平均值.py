"""
easy 2021-12-27 层次遍历ac
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import numpy as np
class Solution:
    def averageOfLevels(self, root: TreeNode):# -> List[float]:
        if not root:return []
        res = []
        q = [root]
        while q:
            cur_level, size = [], len(q)
            total = 0
            for i in range(size):
                node = q.pop(0)
                total += node.val
                cur_level.append(node.val)
                if node.left:q.append(node.left)
                if node.right: q.append(node.right)
            # 退出当前层
            # cur_avg = np.mean(cur_level)
            cur_avg = total/size
            res.append(cur_avg)
        return res

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
    print(Solution().averageOfLevels(a))