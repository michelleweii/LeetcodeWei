"""
middle 二叉树
2021-07-15
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        # 空树不是任意一个树的子结构
        if not A or not B: return False
        if self.is_part(A, B): return True
        return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def is_part(self, p1, p2):
        if not p2: return True
        if not p1: return False
        if p1.val != p2.val: return False
        return self.is_part(p1.left, p2.left) and self.is_part(p1.right, p2.right)

def print_tree(root):
    res = []
    queue = []
    queue.append(root)
    while queue:
        tmp = queue.pop(0)
        res.append(tmp.val)
        if tmp.left:
            queue.append(tmp.left)
        if tmp.right:
            queue.append(tmp.right)
    print(res)

if __name__ == '__main__':
    a = TreeNode(3)
    b = TreeNode(4)
    c = TreeNode(5)
    d = TreeNode(1)
    e = TreeNode(2)
    a.right = c
    a.left = b
    b.right = e
    b.left = d

    g = TreeNode(4)
    h = TreeNode(1)
    g.left = h
    print(print_tree(a))
    print(print_tree(g))
    print(Solution().isSubStructure(a, g))