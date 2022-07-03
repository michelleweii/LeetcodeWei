"""
middle 2022-01-21 树回溯（微信、字节）
# 关键词：“二叉树 双递归”，类似的题目很多 比如LC437、LC04.12、LC563
题目：树中找到与target目标节点距离为k的节点集
https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree/solution/er-cha-shu-zhong-suo-you-ju-chi-wei-kde-nlct0/

# 【方法二】建图+BFS
https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree/solution/gong-shui-san-xie-yi-ti-shuang-jie-jian-x6hak/
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k):# int) -> List[int]:
        hashmap = {} # 构建哈希表，记录每个节点的父亲节点
        # 遍历整个树，记录每个节点的父节点
        def find_father(root):
            if not root:return
            if root.left:
                hashmap[root.left.val] = root
                find_father(root.left)
            if root.right:
                hashmap[root.right.val] = root
                find_father(root.right)

        res = []
        # pre_node要记录它上一步是从何处来的，不走回头路即可
        def dfs(root, pre_node, k):
            # 递归出口
            if k==0: # 找到与target距离为k的点
                res.append(root.val)
                return
            if root.left and root.left != pre_node: #左
                dfs(root.left, root, k-1)
            if root.right and root.right != pre_node: #右
                dfs(root.right, root, k-1)
            # 这一步不太理解？？？
            # 可以往上走，图例5->3
            if root.val in hashmap and hashmap[root.val]!=pre_node: # 根
                dfs(hashmap[root.val], root, k-1)

        # 执行逻辑
        find_father(root)
        # 递归
        dfs(target, None, k)
        return res


if __name__ == '__main__':
    pass