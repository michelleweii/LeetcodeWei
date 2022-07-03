"""
middle 2021-12-07 树形dp
基础题198、213
https://www.programmercarl.com/0337.%E6%89%93%E5%AE%B6%E5%8A%AB%E8%88%8DIII.html#%E6%80%BB%E7%BB%93
本题一定是要后序遍历(左右根)，因为通过递归函数的返回值来做下一步计算。
如果抢了当前节点，两个孩子就不能动，如果没抢当前节点，就可以考虑抢左右孩子（注意这里说的是“考虑”）
- dp数组（dp table）以及下标的含义：下标为0记录不偷该节点所得到的的最大金钱，下标为1记录偷该节点所得到的的最大金钱。
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 树形DP就是在树上进行递归公式的推导
class Solution:
    def rob(self, root: TreeNode):
        if not root:return 0 # 没有node时
        if not root.right and not root.left: return root.val # 只有一个根节点时
        # dp = # 注意这里没有dp数组，遍历树的时候记录结果
        # 长度为2的数组，0：不偷，1：偷
        dp = self.rob_tree(root)
        return max(dp[0],dp[1])

    # 后序遍历
    # 首先明确的是使用后序遍历。 因为通过递归函数的返回值来做下一步计算。
    def rob_tree(self, cur):
        if not cur:return [0, 0] # 确定终止条件，在遍历的过程中，如果遇到空节点的话，很明显，无论偷还是不偷都是0
        left = self.rob_tree(cur.left)
        right = self.rob_tree(cur.right)
        # 偷cur
        # 那么cur的左右孩子要跳过, left[0] + right[0]
        val1 = cur.val + left[0] + right[0]
        # 不偷cur
        val2 = max(left[0], left[1]) + max(right[0], right[1])
        # 如果不偷当前节点，那么左右孩子就可以偷，至于到底偷不偷一定是选一个最大的，
        # 所以：val2 = max(left[0], left[1]) + max(right[0], right[1]);
        return [val2, val1]

"""
【记忆化递归】
class Solution:
    memory = {}
    def rob(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right  is None:
            return root.val
        if self.memory.get(root) is not None:
            return self.memory[root]
        # 偷父节点
        val1 = root.val
        if root.left:
            val1 += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            val1 += self.rob(root.right.left) + self.rob(root.right.right)
        # 不偷父节点
        val2 = self.rob(root.left) + self.rob(root.right)
        self.memory[root] = max(val1, val2)
        return max(val1, val2)
"""

if __name__ == '__main__':
    # root = [3,4,5,1,3,null,1]
    a = TreeNode(3)
    b = TreeNode(4)
    c = TreeNode(5)
    d = TreeNode(3)
    e = TreeNode(1)
    f = TreeNode(1)
    a.right = c
    a.left = b

    b.right = d
    b.left = e

    c.right = f
    print(Solution().rob(a))

