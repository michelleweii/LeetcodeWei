"""
middle 2021-11-02 （快手实习）
https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by--26/
解法1的图解比较容易理解
https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/solution/by-lfool-yq9n/
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 题目要求：其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
# 展开后的单链表应该与二叉树 先序遍历 顺序相同

# 步骤：1、将左子树插入到右子树的地方
#      2、将原来的右子树接到左子树的最右边节点
#      3、考虑新的右子树的根节点，一直重复上边的过程，直到新的右子树为 null
class Solution:
    # 首先我们需要找出【左子树最右边的节点】以便把右子树接过来
    def flatten(self, root: TreeNode) -> None:
        # 左子树为 null，直接考虑下一个节点
        while root: # 注意这里是root不等于空，不是root.left不等于空
            # 如果该节点没有左子树，则移动到右子树上，开始新一轮遍历
            if root.left is None:
                root = root.right
            else:
                # 1、找左子树最右边的节点（案例是4）
                pre = root.left
                while pre.right:
                    pre = pre.right
                # 2、将原来的右子树接到左子树的最右边节点（案例5接到4下面）
                pre.right = root.right
                # 3、将root的左子树插入到右子树的地方（1的right接2）
                root.right = root.left
                root.left = None
                # 4、考虑下一个节点（案例由1移动到2）
                root = root.right
        return
    # 递归版
    # https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/solution/by-thegreatly-yj7g/
    def flatten_dfs(self, root: TreeNode) -> None:
        # 后续遍历
        def dfs(root):
            if not root:return root
            l=dfs(root.left)
            r=dfs(root.right)
            if l:
                l.right=root.right
                root.right=root.left
                root.left=None
            if r:return r
            if l:return l
            return root
        dfs(root)

if __name__ == '__main__':
    pass
    # root = [1, 2, 5, 3, 4, None, 6]
    # print(Solution().flatten(root))
#     [1,null,2,null,3,null,4,null,5,null,6]
