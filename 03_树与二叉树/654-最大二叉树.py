"""
middle 2021-12-28 二叉树构造/二分
将list转为树。构造树一般采用的是前序遍历，因为先构造中间节点，然后递归构造左子树和右子树。
https://leetcode-cn.com/problems/maximum-binary-tree/solution/xiao-ying-wu-654-python-duo-chong-fang-f-8bf3/
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 分治
    def constructMaximumBinaryTree(self, nums): #List[int]) -> TreeNode:
        if not nums:return None
        num = max(nums) # 找到最大值
        root = TreeNode(num)
        index = nums.index(num) # 最大值的下标
        # 递归构造左子树
        root.left = self.constructMaximumBinaryTree(nums[:index])
        # 递归构造右子树
        root.right = self.constructMaximumBinaryTree(nums[index+1:])
        return root
    # 单调栈
    
if __name__ == '__main__':
    nums = [3, 2, 1, 6, 0, 5]
    print(Solution().constructMaximumBinaryTree(nums))