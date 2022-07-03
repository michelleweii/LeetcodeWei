"""
middle 2021-12-14 bst
反中序遍历 相同题lc1038，题目：使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和
累加树：bst中序遍历之后，每个node的值更新为右侧all value+self（所有>=node的总和）
https://leetcode-cn.com/problems/convert-bst-to-greater-tree/solution/shou-hua-tu-jie-zhong-xu-bian-li-fan-xiang-de-by-x/
思路：先递归遍历右子树、后递归遍历左子树；维护一个外部累加变量sum，然后把sum赋值给 BST 中的每一个节点；
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.sum = 0

    def convertBST(self, root): #Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:return root
        self.traverse(root)
        return root

    # 反中序遍历
    def traverse(self, root):
        if not root:return
        self.traverse(root.right)
        self.sum += root.val
        root.val = self.sum
        self.traverse(root.left)

# var convertBST = function(root) {
#   let sum = 0
#   function traversal (root) {
#     if (root !== null) {
#       traversal(root.right)
#       sum += root.val
#       root.val = sum
#       traversal(root.left)
#     }
#   }
#   traversal(root)
#   return root
# }
if __name__ == '__main__':
    pass