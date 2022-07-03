"""
easy 2021-11-11 树回溯
https://programmercarl.com/0112.%E8%B7%AF%E5%BE%84%E6%80%BB%E5%92%8C.html#%E9%80%92%E5%BD%92
回溯:https://leetcode-cn.com/problems/path-sum/solution/lu-jing-zong-he-de-si-chong-jie-fa-dfs-hui-su-bfs-/
"""
"""
if(traversal(cur->left, count - cur->left->val)) return true; // 注意这里有回溯的逻辑
为什么传参的时候直接相减是有回溯逻辑的呢?
回溯隐藏在traversal(cur->left, count - cur->left->val)这里， 
因为把count - cur->left->val 直接作为参数传进去，函数结束，count的数值没有改变。
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:return False
        return self.dfs(root, targetSum-root.val)

    def dfs(self, root, target):
        # 遇到叶子节点，并且计数为0
        if target == 0 and not root.right and not root.left:
            return True
        #  遇到叶子节点，计数不为0
        if not root.right and not root.left:
            return False

        if root.left:
            target -= root.left.val
            if self.dfs(root.left, target):return True # # 递归，处理左节点
            target += root.left.val  # 回溯

        if root.right:
            target -= root.right.val
            if self.dfs(root.right, target):return True # # 递归，处理右节点
            target += root.right.val  # 回溯

        return False

if __name__ == '__main__':
    a = TreeNode(5)
    b = TreeNode(4)
    c = TreeNode(8)
    d = TreeNode(11)
    e = TreeNode(13)
    f = TreeNode(4)
    g = TreeNode(7)
    h = TreeNode(2)
    i = TreeNode(5)
    j = TreeNode(1)
    a.right = c
    a.left = b
    b.left = d
    d.left = g
    d.right = h
    c.right = f
    c.left = e
    f.right = j
    f.left = i
    sum = 22
    print(Solution().hasPathSum(a,sum))




