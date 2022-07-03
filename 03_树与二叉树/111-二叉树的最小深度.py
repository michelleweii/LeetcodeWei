"""
easy 2021-11-11
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
- 叶子节点的定义是左孩子和右孩子都为 null 时叫做叶子节点
- 当 root 节点左右孩子都为空时，返回 1
- 当 root 节点左右孩子有一个为空时，返回不为空的孩子节点的深度
- 当 root 节点左右孩子都不为空时，返回左右孩子较小深度的节点值
https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/solution/li-jie-zhe-dao-ti-de-jie-shu-tiao-jian-by-user7208/
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:return 0
        # 1.左孩子和有孩子都为空的情况，说明到达了叶子节点，直接返回1即可
        if root.left is None and root.right is None: return 1
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        # 2.如果左孩子和右孩子其中一个为空，那么需要返回比较大的那个孩子的深度?
        # 这里没有理解
        # 题目要求是到叶子节点，所以返回比较的大那边，因为另一边不是叶子节点啊
        if root.left is None or root.right is None:return left+right+1
        # 3.最后一种情况，也就是左右孩子都不为空，返回最小深度+1即可
        return min(left,right)+1

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
    print(Solution().minDepth(a))