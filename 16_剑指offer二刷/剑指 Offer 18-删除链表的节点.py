"""
easy 链表+双指针
2021-07-15
https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/solution/mian-shi-ti-18-shan-chu-lian-biao-de-jie-dian-sh-2/
一个节点就ok
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if not head:return head
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
                return dummy.next
            p = p.next
        return dummy.next

if __name__ == '__main__':
    head = ListNode(4)
    b = ListNode(5)
    c = ListNode(1)
    d = ListNode(9)
    head.next = b
    b.next = c
    c.next = d
    val = 1
    print(Solution().deleteNode(head, val))
    # [4,5,9]