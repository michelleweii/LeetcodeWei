"""
easy 2021-12-27 树回溯basic
https://www.programmercarl.com/0257.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%89%80%E6%9C%89%E8%B7%AF%E5%BE%84.html#%E9%80%92%E5%BD%92
再次gg!!!
从根节点到叶子的路径，所以需要前序遍历。
1、递归出口：到达叶子节点；
2、回溯，回溯和递归是一一对应的，有一个递归，就要有一个回溯。
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def binaryTreePaths(self, root: TreeNode):# -> List[str]:
        if not root:return self.res
        self.backtrace(root)
        return self.res

    def backtrace(self, cur):
        self.path.append(str(cur.val)) # 先添加

        # 递归出口：到达叶子节点
        if cur.left is None and cur.right is None:
            self.res.append('->'.join(self.path))

        if cur.left:
            self.backtrace(cur.left)
            self.path.pop() # 回溯和递归是一一对应的，有一个递归，就要有一个回溯。

        if cur.right:
            self.backtrace(cur.right)
            self.path.pop() # 回溯和递归是一一对应的，有一个递归，就要有一个回溯。

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
    print(Solution().binaryTreePaths(a))