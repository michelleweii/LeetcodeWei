
# 2022-02-28
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        # 归并出口
        if not head or not head.next:return head

        # 求中点
        slow, fast = head, head
        while fast and fast.next:
            slow,fast=slow.next, fast.next.next

        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        dummy = h = ListNode(-1)
        while left and right:
            if left.val<right.val:
                h.next = left
                left = left.next
            else:
                h.next = right
                right = right.next
            h = h.next
        h.next = left if left else right
        return dummy.next




if __name__ == '__main__':
    a = ListNode(4)
    b = ListNode(3)
    c = ListNode(1)
    d = ListNode(2)
    print(Solution().sortList(a))
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]