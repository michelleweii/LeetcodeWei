"""
middle 2022-05-13 后序遍历
[递归]https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/solution/by-thegreatly-yj7g/
首先，对于前序遍历，所以最右边的结点一定在链表的最后
对于每一棵子树（设当前子树的根节点为root），我们要做如下三点：
1.左子树前序遍历后的最后一个节点（即root.left的返回值l）的右指针指向root的右子树
2.root的右指针指向root的左子树，因为经过上一步操作右子树的节点已经存在于左子树上。
3.root的左指针赋为空
之后要考虑的一个问题就是我们遍历到某个节点时如何确定其返回值：
因为对于每一棵子树，其左子树的返回值的右指针指向右子树，所以返回值必定等于当前子树前序遍历后最右边的节点
1.所以每次优先返回右子树的遍历结果
2.如果右子树不存在，则返回左子树
3.如果都不存在，返回当前节点
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
2
 \  2)root.right=root.left
  3
   \  1) l.right=root.right
    4
3)root.left=None
"""
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
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