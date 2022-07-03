"""
middle 二叉树
2021-07-16 还需要再看
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, target):
        res = []
        if not root:return res
        self.dfs(res, [], root, target)
        return res

    def dfs(self, res, path, root, target):
        # 定义dfs出口
        if not root: return
        path.append(root.val)
        target -= root.val
        # 一定要是叶子节点，才算走到了末尾。并且target为0
        if not root.left and not root.right and target==0:
            res.append(path[:])
        self.dfs(res, path, root.left, target)
        self.dfs(res, path, root.right, target)
        # 1_回溯算法
        path.pop()


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

    target = 12
    print(Solution().pathSum(a, target))