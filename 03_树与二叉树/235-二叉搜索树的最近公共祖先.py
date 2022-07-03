"""
easy 2021-12-29 bst
https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/solution/mian-shi-ti-68-i-er-cha-sou-suo-shu-de-zui-jin-g-7/
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 二叉搜索树，右边节点比他大，左边节点比他小
# 迭代寻找，若都小于跟结点，迭代去左子树找，若都大于根节点，迭代去右子树找，一大一小就是根节点
class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if not root:return root
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            # p，q 在root的 异侧，返回root节点，跳出循环。
            return root

    # 迭代寻找，若都小于跟结点，迭代去左子树找，若都大于根节点，迭代去右子树找，一大一小就是根节点
    def lowestCommonAncestor_iter(self, root, p, q):
        while root:
            # 当 p, q 都在 root 的 右子树 中，则遍历至 root.right;
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
        return None


if __name__ == '__main__':
    a = TreeNode(6)
    b = TreeNode(2)
    c = TreeNode(8)
    a.left = b
    a.right = c
    # a = TreeNode(6)
    # a = TreeNode(6)
    # a = TreeNode(6)
    # a = TreeNode(6)
    # a = TreeNode(6)
    # a = TreeNode(6)
    # a = TreeNode(6)
    # a = TreeNode(6)
    # a = TreeNode(6)

    # root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    # p = 2
    # q = 8
    print(Solution().lowestCommonAncestor(a, b, c))
