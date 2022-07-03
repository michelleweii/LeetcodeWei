"""
middle 2021-11-06 bst构造
返回所有由 n 个节点组成，从1-n的所有互斥bst
https://leetcode-cn.com/problems/unique-binary-search-trees-ii/solution/cong-gou-jian-dan-ke-shu-dao-gou-jian-suo-you-shu-/
https://leetcode-cn.com/problems/unique-binary-search-trees-ii/solution/di-gui-zhu-xing-jie-shi-python3-by-zhu_shi_fu/
思路：
lc108 是构建一颗bst；这里是如何选择不同的根节点，以构建不同的树和子树。
假设根节点root是x，则左子树的集合为[1,x-1]，右子树的结合为[x+1,n]。利用递归来实现。
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n):
        if n == 0: return []
        return self.build_tree(1, n)

    # 构建bst代码，表示生产[start,end]的所有可能二叉搜索树
    def build_tree(self, start, end):
        all_tress = []
        # 定义递归出口，递归到子树为空的时候，
        if start > end: return [None] # 注意这里，return [None],会给一个None
        # 如果子树不是空，递归所有可能的根节点
        for i in range(start, end + 1):
            # 对每个root，它所有的左子树构建bst
            # 递归构建左子树，并拿到左子树所有可能的根结点列表 left_tree
            left_tree = self.build_tree(start, i - 1)  # x就是i
            # 对每个root，它所有的右子树构建bst
            # 递归构建右子树，并拿到右子树所有可能的根结点列表 right_tree
            right_tree = self.build_tree(i + 1, end)
            # 把所有可能的左右子树与根节点进行拼接
            for left_node in left_tree:
                for right_node in right_tree:
                    root = TreeNode(i)
                    root.left = left_node
                    root.right = right_node
                    all_tress.append(root)
        return all_tress

if __name__ == '__main__':
    n = 3
    print(Solution().generateTrees(n))