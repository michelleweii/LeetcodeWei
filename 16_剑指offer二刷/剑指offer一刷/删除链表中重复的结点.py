# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:return pHead
        dummy = ListNode(-1)
        dummy.next = pHead
        p = dummy
        while p.next:
            # 原来错误是while dummy.next：
            # dummy在while中都没有发生改变，起不到循环结束的作用
            q = p.next
            while (q and p.next.val == q.val):
                q = q.next
            # 如果不存在重复，长度==1
            if p.next.next == q:
                p = p.next
            # 如果存在重复，长度>1
            else: p.next = q
        return dummy.next


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(4)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    print(Solution().deleteDuplication(a))