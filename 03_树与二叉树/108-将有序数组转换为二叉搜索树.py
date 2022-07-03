"""
easy 2021-11-04 bst递归
元素已经升序, 将其转换为一棵"高度平衡"二叉搜索树
已知：BST的中序遍历是升序的。等同于根据中序遍历的序列恢复二叉搜索树
二叉搜索树:对于树中每个节点,若其左子树存在，则其左子树中每个节点的值都不大于该节点值；
若其右子树存在，则其右子树中每个节点的值都不小于该节点值。
平衡:左右子树高度差不超过1。
思路：
1、以升序序列中的任一个元素作为根节点，以该元素左边的升序序列构建左子树，
2、以该元素右边的升序序列构建右子树，这样得到的树就是一棵二叉搜索树啦。
3、又因为本题要求高度平衡，因此我们需要选择升序序列的中间元素作为根节点
https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/solution/jian-dan-di-gui-bi-xu-miao-dong-by-sweetiee/
"""
"""
扩展：
109. 有序链表转换二叉搜索树 将本题的数组换成了链表，做法完全一样，
不过链表无法像数组一样直接索引到中间元素，链表找中间节点可以用快慢指针法，
详见 876. 链表的中间结点。
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:return nums
        # 找到中点，左边升序作为右子树，右边升序作为左子树
        return self.dfs(nums, 0, len(nums)-1)

    def dfs(self, nums, start, end):
        if start>end:return
        # 以升序数组的中间元素作为根节点 root
        mid = start + (end - start) // 2 # 等价于 int mid = (start + end) / 2
        root = TreeNode(nums[mid])
        root.left = self.dfs(nums, start, mid-1)
        root.right = self.dfs(nums, mid+1, end)
        return root

if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    print(Solution().sortedArrayToBST(nums))