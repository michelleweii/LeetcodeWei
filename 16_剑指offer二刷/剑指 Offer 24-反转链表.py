"""
easy 2021-07-15 链表
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        if not head or not head.next: return head
        # 反转链表需要3个节点
        prev = None
        cur = head
        while cur:
            tail = cur.next
            cur.next = prev
            prev = cur
            cur = tail
        # self.print_link(prev)
        return prev

    def print_link(self, head):
        p = head
        rs = []
        while p:
            rs.append(p.val)
            p = p.next
        print(rs)

if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    print(Solution().reverseList(a))
