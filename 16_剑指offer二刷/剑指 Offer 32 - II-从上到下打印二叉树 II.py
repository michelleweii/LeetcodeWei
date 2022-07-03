"""
easy 二叉树
2021-07-15
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # [
    #   [3],
    #   [9,20],
    #   [15,7]
    # ]
    def levelOrder(self, root):
        if not root:return []
        queue = []
        res = []
        queue.append(root)
        while queue:
            cur_level, size = [], len(queue)
            for i in range(size):
                tmp = queue.pop(0)
                cur_level.append(tmp.val)
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
            res.append(cur_level[:])
        return res

if __name__ == '__main__':
    a = TreeNode(3)
    b = TreeNode(5)
    c = TreeNode(6)
    d = TreeNode(2)
    g = TreeNode(1)
    a.right = g
    a.left = b
    b.right = d
    b.left = c
    print(Solution().levelOrder(a))
