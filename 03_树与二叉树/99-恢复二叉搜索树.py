"""
middle 2021-11-07 bst构造
将一棵树恢复成bst
(好)https://leetcode-cn.com/problems/recover-binary-search-tree/solution/tu-jie-hui-fu-yi-ge-er-cha-sou-suo-shu-by-hyj8/
https://leetcode-cn.com/problems/recover-binary-search-tree/solution/zhong-xu-bian-li-by-powcai/
错误1：出现了两对不满足前小后大，需要交换第一对的第一个元素与第二对的第二个元素。
错误2：只出现一对不满足前小后大，交换这一对元素即可。
思路：只用比较前后访问的节点值，prev 保存上一个访问的节点，当前访问的是 root 节点。
每访问一个节点，如果prev.val>=root.val，就找到了一对“错误对”。
检查一下它是第一对错误对，还是第二对错误对。
遍历结束，就确定了待交换的两个错误点，进行交换。
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.first_node, self.second_node = None, None # 错误对
        self.pre_node = TreeNode(float("-inf"))

    def recoverTree(self, root):
        if not root:return root
        self.in_order(root)
        self.first_node.val, self.second_node.val = self.second_node.val, self.first_node.val

    # 二叉树中序遍历（左根右）
    def in_order(self, root):
        if not root:return root # return 也可以
        # 左
        self.in_order(root.left)
        # 根（处理）
        # 只出现一对不满足前小后大，交换这一对元素即可。
        if self.first_node is None and self.pre_node.val >= root.val:
            self.first_node = self.pre_node
        # 出现了两对不满足前小后大，需要交换第一对的第一个元素与第二对的第二个元素。
        if self.first_node and self.pre_node.val >= root.val:
            self.second_node = root
        self.pre_node = root # 把当前结点设为中序前驱
        # 右
        self.in_order(root.right)

if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(3)
    c = TreeNode(2)
    a.left = b
    b.right = c
    print(Solution().recoverTree(a))