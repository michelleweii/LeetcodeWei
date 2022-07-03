
# 2022-02-28
# https://leetcode-cn.com/problems/linked-list-cycle-ii/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:return
        # 先求第一次相遇点
        slow,fast = head,head
        while fast and fast.next:
            slow,fast = slow.next,fast.next.next
            if not fast or not fast.next:return # 无环的情况
            if slow==fast:
                break
        # slow 是相遇点
        # 找到第一次相遇点，再次走a步，找到环入口位置
        fast = head
        while fast != slow:
            slow,fast=slow.next,fast.next
        return slow

if __name__ == '__main__':
    a = ListNode(3)
    b = ListNode(2)
    c = ListNode(0)
    d = ListNode(-4)
    a.next = b
    b.next = c
    c.next = d
    d.next = b
    print(Solution().detectCycle(a).val)