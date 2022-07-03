# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):

        p1 = pHead #slow
        p2 = pHead #fast
        meet = pHead
        flag = 0
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                flag = 1
                meet = p1
                break
        if not flag:
            return None

        start = pHead
        while meet and start:
            if meet == start:
                return start
            meet = meet.next
            start = start.next
        return None

if __name__ == '__main__':
    a = ListNode(3)
    b = ListNode(2)
    c = ListNode(0)
    d = ListNode(-4)
    a.next = b
    b.next = c
    c.next = d
    d.next = b
    print(Solution().EntryNodeOfLoop(a))