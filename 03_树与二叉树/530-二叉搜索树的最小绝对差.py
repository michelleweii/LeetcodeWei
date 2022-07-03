"""
easy 2021-12-29 bst遍历
https://www.programmercarl.com/0530.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E6%9C%80%E5%B0%8F%E7%BB%9D%E5%AF%B9%E5%B7%AE.html
遇到在二叉搜索树上求什么最值啊，差值之类的，就把它想成在一个有序数组上求最值，求差值，这样就简单多了。
在一个有序数组上求两个数最小差值。
"""
import sys
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.res = sys.maxsize
        self.pre = None

    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root: return 0
        self.dfs(root)
        return self.res

    def dfs(self, cur):
        if not cur: return
        # if cur.left:
        self.dfs(cur.left)  # 左
        # 根处理操作
        if self.pre:
            # print(self.pre.val, cur.val, self.res)
            # cur.val-self.pre.val 不需要abs，因为中序bst是升序的
            self.res = min(self.res, cur.val - self.pre.val)
        self.pre = cur  # 记录前一个
        # if cur.right:
        self.dfs(cur.right)  # 右

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
    print(Solution().getMinimumDifference(a))