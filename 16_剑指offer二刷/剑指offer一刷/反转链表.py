# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def ReverseList(self, pHead):
        # 反转链表需要三个listnode
        pre = None
        cur = pHead
        while cur:
            tail = cur.next
            cur.next = pre
            pre = cur
            cur = tail
        # return cur # cur目前指的是空
        return pre

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
    print(Solution().ReverseList(a))

"""
      if pHead is None or pHead.next is None:
            return pHead
        # 声明一个空节点
        pre = None
        cur = pHead
        while cur:
            tail = cur.next
            cur.next = pre
            pre = cur
            cur = tail
        return pre
    
"""