"""
middle 链表(将二叉搜索树改为双向链表)
2021-07-26
https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/solution/mian-shi-ti-36-er-cha-sou-suo-shu-yu-shuang-xian-5/
"""
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return root
        self.pre = None
        self.dfs(root)
        self.head.left, self.pre.right = self.pre, self.head # right、left可以修改的
        return self.head

    def dfs(self, cur):
        if not cur: return
        self.dfs(cur.left)  # 递归左子树

        if self.pre:  # 修改节点引用
            self.pre.right, cur.left = cur, self.pre # right、left可以修改的
        else:  # 记录头节点
            self.head = cur
        self.pre = cur  # 保存 cur

        self.dfs(cur.right)  # 递归右子树

if __name__ == '__main__':
    n = 10
    print(Solution().treeToDoublyList(n))