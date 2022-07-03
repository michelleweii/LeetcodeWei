"""
middle 2021-11-06 遍历
已知：BST的中序遍历是升序的
https://leetcode-cn.com/problems/validate-binary-search-tree/solution/wu-xing-dai-ma-qing-song-gao-ding-yan-zh-16b5/
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# # 方法一：中序遍历二叉树，结果是否是递增的，递增代表是二叉搜索树。
# 可以不将一棵树遍历完，在遍历过程中进行判断。全部遍历完太傻了啊。
class Solution(object):
    # class Solution {
    #     long pre = Long.MIN_VALUE;
    #     public boolean isValidBST(TreeNode root) {
    #         if (root == null) {
    #             return true;
    #         }
    #         // 访问左子树
    #         if (!isValidBST(root.left)) {
    #             return false;
    #         }
    #         // 访问当前节点：如果当前节点小于等于中序遍历的前一个节点，说明不满足BST，返回 false；否则继续遍历。
    #         if (root.val <= pre) {
    #             return false;
    #         }
    #         pre = root.val;
    #         // 访问右子树
    #         return isValidBST(root.right);
    #     }
    # }

    def isValidBST1(self, root):
        if not root:return root
        res = [] # 存中序遍历的结果
        self.helper(root, res)
        for i in range(1, len(res)):
            if res[i-1] >= res[i]:
                return False
        return True

    def helper(self,root,res):
        # 二叉树中序遍历
        if not root:return root
        self.helper(root.left, res)
        res.append(root.val)
        # print(res)
        self.helper(root.right, res)


# 方法二，递归版本，每个结点都满足左小于它，右大于它的性质
#     二叉搜索树的性质就是左子树中所有节点的值都小于根节点，右子树中所有节点的值都大于根节点
#     直接递归，验证左子树的时候，将左子树值的最小范围和最大范围作为参数传入，同理右子树也是如此
    def isValidBST(self, root):
        return self.check_bst(root, float("-inf"), float("inf"))

    # 限定以 root 为根的子树节点必须满足 max.val > root.val > min.val
    def check_bst(self, node, left, right):
        # 如果是空节点
        if not node: return True
        # 若 root.val 不符合 max 和 min 的限制，说明不是合法 BST
        if not left < node.val < right:
            return False
        # 左子树分别bst
        # 右子树分别bst，后面两个参数不是很理解（最小范围、最大范围）
        # 限定左子树的最大值是 root.val，右子树的最小值是 root.val
        return (self.check_bst(node.left, left, node.val)
                and self.check_bst(node.right, node.val, right))

if __name__ == '__main__':
    a = TreeNode(2)
    b = TreeNode(1)
    c = TreeNode(3)
    # d = TreeNode(3)
    # e = TreeNode(6)
    a.right = c
    a.left = b
    # c.right = e
    # c.left = d

    print(Solution().isValidBST(a))