"""
easy 2021-07-18 bst
"""
"""
本文解法基于此性质：二叉搜索树的中序遍历为 递增序列 。
根据以上性质，易得二叉搜索树的 中序遍历倒序 为 递减序列 。
因此，求 “二叉搜索树第 k 大的节点” 可转化为求 “此树的中序遍历倒序的第 k 个节点”。

链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/solution/mian-shi-ti-54-er-cha-sou-suo-shu-de-di-k-da-jie-d/
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        if not root: return 0
        self.k = k
        self.dfs(root)
        return self.res
    # 注意这里 k 需要是全局变量。
    def dfs(self, root):
        if not root:return
        # 右根左遍历
        self.dfs(root.right)
        if self.k==0:return
        self.k-=1
        if self.k==0:self.res=root.val
        self.dfs(root.left)

    def kthLargest2022(self, root: TreeNode, k: int) -> int:
        if not root: return 0
        self.k = k
        self.dfs2022(root)
        return self.res

    def dfs2022(self, root):
        if not root:return
        # 右根左遍历
        if root.right and self.k: self.dfs(root.right)
        # if self.k==0:return
        self.k -= 1
        if self.k==0:self.res=root.val
        if root.left and self.k: self.dfs(root.left)



if __name__ == '__main__':
    root = [3, 1, 4, None, 2]
    k = 1
    # print(Solution().kthLargest(root, k))
