"""
middle 2021-12-28 二叉树构造/单调栈（不是自己做的嗯）
将list转为树。构造树一般采用的是前序遍历，因为先构造中间节点，然后递归构造左子树和右子树。
https://leetcode-cn.com/problems/maximum-binary-tree/solution/xiao-ying-wu-654-python-duo-chong-fang-f-8bf3/
"""
"""
对于找最近一个比当前值大/小的问题，都可以使用单调栈来解决。
在这个题中，我们要找到元素右边第一个比它大的元素作为整个左侧区间的根结点，因此我们可以维护一个 递减栈，
存放未找到右侧更大元素的元素。

遍历nums，构造结点，当 栈顶元素找到更大元素 时，将栈内小于这个更大元素的元素出栈，连接起来（上面元素是下面元素的右孩子），最后一个出栈的元素，作为这个更大元素的左孩子。
遍历结束后，栈内元素再次出栈相连（上面元素是下面元素的右孩子），并返回栈底元素（nums的最大值，也就是根结点）
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 单调栈
    def constructMaximumBinaryTree(self, nums): #List[int]) -> TreeNode:
        stack = []
        for num in nums:
            root = TreeNode(num)
            pre = None
            while stack and root.val > stack[-1].val:
                cur = stack.pop()
                cur.right = pre
                pre = cur
            root.left = pre
            stack.append(root)

        pre, cur = None, None
        while stack:
            cur = stack.pop()
            cur.right = pre
            pre = cur

        return cur
    # 分治

if __name__ == '__main__':
    nums = [3, 2, 1, 6, 0, 5]
    print(Solution().constructMaximumBinaryTree(nums))