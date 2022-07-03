"""
easy 2021-12-28 递归遍历（还没太理解）
https://leetcode-cn.com/problems/binary-tree-tilt/solution/gong-shui-san-xie-jian-dan-er-cha-shu-di-ekz4/
一个树的节点的坡度：该节点(左子树的结点之和)-(右子树结点之和)的绝对值。空结点的的坡度是0。
整个树的坡度就是其所有节点的坡度之和。
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.res = 0

    def findTilt_on(self, root):
        if not root: return 0
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:return 0
        # 在计算子树权值和的时候将坡度进行累加
        l = self.dfs(root.left) # 左子树权值和
        r = self.dfs(root.right)
        self.res += abs(l-r)
        return l+r+root.val

    # O(n^2)
    def findTilt(self, root):
        # 1、计算子树坡度
        if not root:return 0
        # 左子树坡度
        left_tilt = self.findTilt(root.left)
        # 右子树坡度
        right_tilt = self.findTilt(root.right)
        # 差值
        diff = abs(self.get_sum(root.left)-self.get_sum(root.right))
        return left_tilt+right_tilt+diff
    # 2、计算子树权值和
    # 求该节点+左右子树总和
    def get_sum(self, root):
        if not root:return 0
        return self.get_sum(root.left)+self.get_sum(root.right)+root.val

if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    a.left = b
    a.right = c
    c.right = d
    d.right = e
    ans = Solution()
    print(ans.findTilt(a))
    # 5+9+10 = 24
