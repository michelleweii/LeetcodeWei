"""
middle 2021-11-04 层次遍历-
自底向上的层序遍历(最终结果逆序一下)
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root):
        if not root:return []
        queue,res = [],[]
        if root:
            queue.append(root)
            while queue:
                cur_level,size = [],len(queue)
                for _ in range(size):
                    cur = queue.pop(0)
                    cur_level.append(cur.val)
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                res.append(cur_level)
        return res[::-1]

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
    print(Solution().levelOrderBottom(a))