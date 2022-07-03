"""
middle 2021-12-16 bi-tree中序遍历-迭代版
基本思路：这道题本质上考的是「将迭代版的中序遍历代码」做等价拆分。
【中序遍历迭代法】https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/die-dai-fa-by-jason-2/
1、中序遍历的基本逻辑是：处理左子树 -> 处理当前节点 -> 处理右子树。
2、其中迭代做法是利用「栈」进行处理：
2.1 先将当前节点的所有左子树压入栈，压到没有为止
2.2 将最后一个压入的节点弹出（栈顶元素），加入答案
2.3 将当前弹出的节点作为当前节点，重复步骤一

# ---------------------------------- hihi -------------------------------
BST 的中序迭代时就是维护了一个单调递减栈！
https://leetcode-cn.com/problems/binary-search-tree-iterator/solution/fu-xue-ming-zhu-dan-diao-zhan-die-dai-la-dkrm/
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    # 这种中序遍历迭代好理解一点
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        cur = self.stack.pop()
        node = cur.right
        while node:
            self.stack.append(node)
            node = node.left
        return cur.val

    def hasNext(self):
        return bool(self.stack)

    # def __init__(self, root: TreeNode):
    #     self.stack = []
    #     self.stack.append(root)
    #     # 先将当前节点的所有左子树压入栈，压到没有为止
    #     while self.stack[-1].left:
    #         self.stack.append(self.stack[-1].left)
    #
    # def next(self) -> int:
    #     """
    #     int next()将指针向右移动，然后返回指针处的数字。
    #     翻译一下，就是返回中序遍历的结果
    #     """
    #     # 将最后一个压入的节点弹出（栈顶元素），加入答案
    #     res = self.stack.pop() # 根
    #     # 访问右子树
    #     if res.right:
    #         self.stack.append(res.right)
    #         while self.stack[-1].left:
    #             self.stack.append(self.stack[-1].left)
    #     return res.val
    #
    # def hasNext(self) -> bool:
    #     """
    #     boolean hasNext() 如果向指针右侧遍历存在数字，则返回 true；否则返回 false。
    #     翻译一下，如果
    #     """
    #     return bool(self.stack)
"""
# 既然是考察中序遍历，那么就将中序遍历的结果用dfs做一遍，保存在queue里
# 调用next()时，返回队首元素；
# 如果队不空，调动hashnext()即可返回Ture
def __init__(self, root: TreeNode):
    self.queue = []
    def dfs(root):
        if root:
            dfs(root.left)
            self.queue.append(root)
            dfs(root.right)
    dfs(root)
def next(self) -> int:
    ans = self.queue.pop(0)
    return ans.val
def hasNext(self) -> bool:
    return True if self.queue else False
"""
if __name__ == '__main__':
    a = TreeNode(7)
    b = TreeNode(3)
    c = TreeNode(15)
    d = TreeNode(9)
    e = TreeNode(20)
    a.right = c
    a.left = b
    c.right = e
    c.left = d
    obj = BSTIterator(a)
    param_1 = obj.next()
    param_2 = obj.hasNext()