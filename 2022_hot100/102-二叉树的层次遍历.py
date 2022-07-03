"""
easy 2021-12-25 层次遍历基础基础！
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Solution(object):
    # 2020/12/23
    def levelOrder(self, root: TreeNode):# -> List[List[int]]:
        if root is None:return []
        queue, path = deque([root]), []
        while queue:
            cur_level, size = [], len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur_level.append(node.val)
            path.append(cur_level[:])
        return path

    def levelOrder2(self, root):
        queue = []
        rs = []
        if root:
            queue.append(root)
            while queue:
                cur_level,size = [],len(queue)
                for _ in range(size):
                    tmp = queue.pop(0)
                    cur_level.append(tmp.val)
                    if tmp.left:
                        queue.append(tmp.left)
                    if tmp.right:
                        queue.append(tmp.right)
                rs.append(cur_level[:])
        return rs

    # 深度优先遍历
    def dfs(self,root):
        stack = []
        rs = []
        if root:
            stack.append(root)
            while stack:
                cur = stack.pop()
                rs.append(cur.val)
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
        print(rs)

    def depth_tree(self,root):
        lst = []
        lst.append(root)
        while len(lst) > 0:
            node = lst.pop()
            print(node.val)
            if node.right is not None:
                lst.append(node.right)
            if node.left is not None:
                lst.append(node.left)


if __name__ == '__main__':
    # a = TreeNode(3)
    # b = TreeNode(9)
    # c = TreeNode(20)
    # d = TreeNode(15)
    # e = TreeNode(7)
    # a.right = c
    # a.left = b
    # c.right = e
    # c.left = d

    a = TreeNode(3)
    b = TreeNode(5)
    c = TreeNode(6)
    d = TreeNode(2)
    e = TreeNode(7)
    f = TreeNode(4)
    g = TreeNode(1)
    h = TreeNode(0)
    i = TreeNode(8)
    # j = TreeNode(1)
    a.right = g
    a.left = b
    b.left = c
    b.right = d
    d.left = e
    d.right = f
    c.right = f
    c.left = e
    g.right = i
    g.left = h
    print(Solution().levelOrder(a))
    print(Solution().dfs(a))
    print(Solution().depth_tree(a))

