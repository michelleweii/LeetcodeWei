"""
middle 2021-12-27 树回溯
题目：找出该二叉树的 最底层 最左边 节点的值。
层次遍历ac；递归不太会(主要思路：不断向下求最大深度，更新最大深度的时候同时更新左下角的值)

在树的最后一行找到最左边的值->深度最大的叶子节点一定是最后一行
https://www.programmercarl.com/0513.%E6%89%BE%E6%A0%91%E5%B7%A6%E4%B8%8B%E8%A7%92%E7%9A%84%E5%80%BC.html#%E9%80%92%E5%BD%92
递归三部曲：
确定递归函数的参数和返回值
参数必须有要遍历的树的根节点，还有就是一个int型的变量用来记录最长深度。 这里就不需要返回值了，所以递归函数的返回类型为void。
本题还需要类里的两个全局变量，maxLen用来记录最大深度，maxleftValue记录最大深度最左节点的数值。

对递归函数什么时候要有返回值，什么时候不能有返回值很迷茫。
=>如果需要遍历整颗树，递归函数就不能有返回值。如果需要遍历某一条固定路线，递归函数就一定要有返回值！
=>本题我们是要遍历整个树找到最深的叶子节点，需要遍历整颗树，所以递归函数没有返回值。
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.maxdepth = 0 # 全局变量 记录最大深度
        self.maxleftvalue = 0 # 全局变量 最大深度最左节点的数值
    # 主要思路：
    # 不断向下求最大深度，更新最大深度的时候同时更新左下角的值
    def findBottomLeftValue(self, root):
        if not root.left and not root.right:return root.val # 只有一个节点时
        self.traversal(root, 0) # cur_depth标记现在节点的深度
        return self.maxleftvalue

    def traversal(self, root, cur_depth):
        # 求最左节点，前序遍历
        # 当遇到叶子节点的时候，就需要统计一下最大的深度了，所以需要遇到叶子节点来更新最大深度。
        if not root.left and not root.right:
            if cur_depth>self.maxdepth:
                self.maxdepth = cur_depth
                self.maxleftvalue = root.val
            return

        if root.left:
            cur_depth += 1
            self.traversal(root.left, cur_depth)
            # 隐藏回溯写法
            # self.traversal(root.left, cur_depth+1)
            cur_depth -= 1 # 回溯

        if root.right:
            cur_depth += 1
            self.traversal(root.right, cur_depth)
            cur_depth -= 1 # 回溯

    # myself ac
    def findBottomLeftValue_level(self, root):  #Optional[TreeNode]) -> int:
        if not root:return
        ans = 0
        q = [root]
        while q:
            cur_level, size = [], len(q)
            for i in range(size):
                node = q.pop(0)
                cur_level.append(node.val)
                if node.left:q.append(node.left)
                if node.right: q.append(node.right)
            ans = cur_level[0]
        return ans

if __name__ == '__main__':
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    d = TreeNode(15)
    e = TreeNode(7)
    a.right = c
    a.left = b
    c.right = e
    c.left = d
    print(Solution().findBottomLeftValue(a))