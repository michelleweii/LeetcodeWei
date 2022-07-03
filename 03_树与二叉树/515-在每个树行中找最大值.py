"""
middle 2021-12-27 层次遍历ac
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root): #Optional[TreeNode]) -> List[int]:
        if not root:return []
        q, res = [root], []
        while q:
            cur_level, size = [], len(q)
            maxvalue = float('-inf')# 定义每一层的最大值
            for i in range(size):
                node = q.pop(0)
                maxvalue = node.val if node.val>maxvalue else maxvalue
                if node.left:q.append(node.left)
                if node.right: q.append(node.right)
            # 退出当前层遍历
            res.append(maxvalue)
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
    print(Solution().largestValues(a))