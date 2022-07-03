# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head:return head
        p = head
        cnt = 0
        while p:
            cnt += 1
            p = p.next
        if k>cnt:return
        n = cnt-k+1
        dummy = ListNode(-1)
        dummy.next = head
        q = dummy
        cnt = 0
        while q.next:
            cnt += 1
            if cnt==n:
                return q.next.val
            q = q.next

# 删除倒k呢？

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    k = 1
    print(Solution().FindKthToTail(a,k))