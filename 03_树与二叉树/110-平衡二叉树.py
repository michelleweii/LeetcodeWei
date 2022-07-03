"""
easy 2021-11-06 平衡二叉树
https://leetcode-cn.com/problems/balanced-binary-tree/solution/balanced-binary-tree-di-gui-fang-fa-by-jin40789108/
# 暴力思路：
1、判断 当前子树 是否是平衡树；and
2、判断 当前子树的左子树 是否是平衡树；and
3、判断 当前子树的右子树 是否是平衡树；
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 2021-12-25, 从底至顶（提前阻断），先序遍历，时间复杂度 O(N)
    # 思路是对二叉树做先序遍历，从底至顶返回子树最大高度，若判定某子树不是平衡树则 “剪枝” ，直接向上返回。
    def isBalanced(self, root: TreeNode) -> bool:
        return self.isAvl(root) != -1

    def isAvl(self, root):
        if not root: return 0
        left = self.isAvl(root.left) # 左
        if left == -1: return -1
        right = self.isAvl(root.right) # 右
        if right == -1: return -1
        # 以当前节点为根节点的树的最大高度
        return max(left, right) + 1 if abs(left - right) < 2 else -1 # 根

    # 从顶至底（暴力法）
    def isBalanced_old(self, root):
        if not root:return True
        elif abs(self.depth(root.left) - self.depth(root.right)) > 1:
            return False
        # 以下没想到，需要左子树和右子树同时满足是平衡二叉树的条件
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    # 从顶至底（暴力法）
    # 求树高度
    def depth(self, root):
        if not root: return 0
        # 左子树高度
        LD = self.depth(root.left)
        # 右子树高度
        RD = self.depth(root.right)
        return max(RD, LD) + 1 # +1是根节点也要计算

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
    print(Solution().isBalanced(a))