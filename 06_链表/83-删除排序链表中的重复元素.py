"""
easy 2021-12-21 链表
有重复元素just删除一个
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        pre = head
        cur = pre.next
        while cur != None:
            if pre.val == cur.val:
                pre.next = cur.next
                cur = pre.next
            else:
                pre = cur
                cur = pre.next
        return head

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(1)
    c = ListNode(2)
    a.next = b
    b.next = c
    print(Solution().deleteDuplicates(a))
