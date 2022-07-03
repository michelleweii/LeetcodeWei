# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        p1,p2 = None,None
        rs = None
        head = rs
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                rs.next = pHead1
                pHead1 = pHead1.next
            else:
                rs.next = pHead2
                pHead2 = pHead2
            rs = rs.next
        while pHead1:
            rs.next = pHead1
        while pHead2:
            rs.next = pHead2
        return head
