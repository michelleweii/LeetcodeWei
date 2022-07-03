# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1:return pHead1
        if not pHead2:return pHead2
        len1 = self.getLength(pHead1)
        len2 = self.getLength(pHead2)
        diff = abs(len1-len2)
        p1 = pHead1
        p2 = pHead2
        if len1>len2:
            while diff>0:
                diff -= 1
                p1= p1.next
        if len1<len2:
            while diff>0:
                diff -= 1
                p2 = p2.next
        # print(p1.val)
        # print(p2.val)
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1

    def getLength(self,head):
        cnt = 0
        cur = head
        while cur:
            cnt+=1
            cur = cur.next
        return cnt


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next = b
    b.next = c
    d = ListNode(4)
    e = ListNode(5)
    f = ListNode(6)
    d.next = e
    e.next = f
    c.next = e
    print(Solution().FindFirstCommonNode(a,d))