"""
middle 2021-12-29
https://www.programmercarl.com/0450.%E5%88%A0%E9%99%A4%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B9.html
"""
# 第一种情况：没找到删除的节点，遍历到空节点直接返回了
# 找到删除的节点
# 第二种情况：左右孩子都为空（叶子节点），直接删除节点， 返回NULL为根节点
# 第三种情况：删除节点的左孩子为空，右孩子不为空，删除节点，右孩子补位，返回右孩子为根节点
# 第四种情况：删除节点的右孩子为空，左孩子不为空，删除节点，左孩子补位，返回左孩子为根节点
# 第五种情况：左右孩子节点都不为空，则将删除节点的左子树头结点（左孩子）放到删除节点的右子树的最左面节点的左孩子上，返回删除节点右孩子为新的根节点。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root, key: int):# -> Optional[TreeNode]:
        # 第一种情况：没找到删除的节点，遍历到空节点直接返回了
        if not root:return root
        # 找到了，分情况讨论
        if root.val==key:
            # 第二种情况：左右孩子都为空（叶子节点），直接删除节点， 返回NULL为根节点
            if not root.right and not root.left:
                del root
                return None
            # 第三种情况：其左孩子为空，右孩子不为空，删除节点，右孩子补位 ，返回右孩子为根节点
            elif not root.left:
                new_node = root.right
                del root
                return new_node
            # 第四种情况：其右孩子为空，左孩子不为空，删除节点，左孩子补位，返回左孩子为根节点
            elif not root.right:
                new_node = root.left
                del root
                return new_node
            # // 第五种情况：左右孩子节点都不为空，则将删除节点的左子树放到删除节点的右子树的最左面节点的左孩子的位置
            # // 并返回删除节点右孩子为新的根节点。
            # case5要看图
            else:
                # 找到右子树最左面的节点
                cur = root.right
                while cur.left:
                    cur = cur.left
                # 把要删除的节点（root）左子树放在cur的左孩子的位置
                cur.left = root.left
                tmp = root # 把root节点保存一下，下面来删除
                root = root.right # 返回旧root的右孩子作为新root
                del tmp # 释放节点内存
                return root

        if root.val > key: root.left = self.deleteNode(root.left, key)
        if root.val < key: root.right = self.deleteNode(root.right, key)
        return root

if __name__ == '__main__':
    pass