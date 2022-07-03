"""
middle 2021-11-09 链表
借助虚拟头结点。small链表按顺序存储所有小于 x 的节点, large链表按顺序存储所有大于等于 x 的节点;
遍历完原链表后，将 small 链表尾节点指向 large 链表的头节点即能完成对链表的分隔。
时间复杂度: O(n)，其中n是原链表的长度。我们对该链表进行了一次遍历。
空间复杂度: O(1)
https://leetcode-cn.com/problems/partition-list/solution/leetcode86-fen-ge-lian-biao-by-ying-185-1y02/
"""
# 2021-12-21 类似lc328
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next:return head
        small_dummy, large_dummy = ListNode(-1), ListNode(-1)
        small, large = small_dummy, large_dummy
        while head:
            if head.val<x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next
        small.next = large_dummy.next
        large.next = None
        return small_dummy.next


if __name__ == '__main__':
    head = [1, 4, 3, 2, 5, 2]
    a = ListNode(1)
    b = ListNode(4)
    c = ListNode(3)
    d = ListNode(2)
    e = ListNode(5)
    f = ListNode(2)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    x = 3
    print(Solution().partition(a,x))