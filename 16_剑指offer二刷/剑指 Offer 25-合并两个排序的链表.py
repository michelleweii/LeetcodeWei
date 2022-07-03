"""
easy 链表
2021-07-15
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        head = ListNode(-1)
        p = head
        p1 = l1
        p2 = l2
        while p1 and p2:
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next

        if p1:
            p.next = p1
        elif p2:
            p.next = p2

        self.printList(head.next)
        return head.next


    def printList(self,head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        print(res)


if __name__ == '__main__':
    l1 = ListNode(2)
    a = ListNode(3)
    b = ListNode(4)
    l1.next = a
    a.next = b
    l2 = ListNode(1)
    c = ListNode(3)
    d = ListNode(5)
    l2.next = c
    c.next = d
    print(Solution().mergeTwoLists(l1,l2))

"""
p = ListNode(0)
head = p
while l1 and l2:
    if l1.val<l2.val:
        p.next = l1
        l1 = l1.next
        p = p.next
    else:
        p.next = l2
        l2 = l2.next
        p = p.next
if l1:
    p.next = l1
if l2:
    p.next = l2

head = head.next
# self.printList(head)
return head
"""