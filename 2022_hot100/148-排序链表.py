"""
middle 2021-11-03 归并排序（链表版）
题目：对链表进行升序，且O(nlogn)，
回顾下nlogn的排序有哪些？快排、希尔、归并、堆排序
空间复杂度O(1) 希尔、堆排序
https://leetcode-cn.com/problems/sort-list/solution/sort-list-gui-bing-pai-xu-lian-biao-by-jyd/
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 进阶
    def sortList(self, head): # 归并递归（从下到上）空间复杂度O(1)
        pass

    # 朴素版
    def sortList_rec(self, head): # 归并递归（从上到下）空间复杂度O(n)
        if not head or not head.next:return head # 递归出口
        # 和归并list排序不一样的地方
        # 找到中间点，并将链表分成两端，注意这里[链表寻找中间点]的方法。相关lc876
        # slow, fast = head, head.next
        # # 为什么fast=head.next 而不能是fast=head? 也可以
        # # 因为这样长度为2的那一支链表会一直递归下去，直到栈溢出。
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next # 中点 slow
        # mid = slow.next # 也可以mid=show, pre.next=None, 和109一样，标记pre
        # slow.next = None
        slow,fast=head,head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        mid=slow.next
        slow.next=None

        # 归并【递归】，以下都可以理解
        left, right = self.sortList(head), self.sortList(mid)
        # merge `left` and `right` linked list and return it.
        # 辅助ListNode h 作为头部
        h = res = ListNode(0)
        while left and right:
            if left.val<right.val:h.next,left = left,left.next
            else: h.next, right = right,right.next
            h = h.next

        h.next = left if left else right
        return res.next

if __name__ == '__main__':
    a = ListNode(4)
    b = ListNode(2)
    c = ListNode(1)
    d = ListNode(3)
    a.next = b
    b.next = c
    c.next = d
    print(Solution().sortList(a))