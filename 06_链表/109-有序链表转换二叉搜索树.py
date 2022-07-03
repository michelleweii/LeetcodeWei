"""
middle 2021-11-04
与lc108类似。
https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/solution/109-you-xu-lian-biao-zhuan-huan-er-cha-s-nrb7/
思路一：分治+递归先序遍历
1.找到链表的中间节点作为当前平衡二叉搜索树的根节点，并拆分链表为左右部分（作为当前根基节点的左右子树的节点）。
2.递归将拆分的左、右链表分别做序号1.中的处理。
3.返回当前的子树根节点
"""
# 2021-12-22
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head):
        if not head: return head
        if not head.next:  return TreeNode(head.val)
        # 利用快慢指针找到链表中点
        # 找到链表的中间节点作为平衡二叉搜索树的根节点
        slow, fast = head, head
        pre = head
        while fast and fast.next:
            pre = slow
            slow, fast = slow.next, fast.next.next
        mid = slow
        # 生成当前子树的根节点
        root = TreeNode(mid.val)
        # 拆分左右链表
        pre.next = None # 左子树断开
        rhead = slow.next
        # 递归先序遍历构建平衡二叉搜索树
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(rhead)
        return root

if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    print(Solution().sortedListToBST(nums))
