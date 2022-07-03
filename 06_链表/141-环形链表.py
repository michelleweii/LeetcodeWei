"""
easy 2021-12-23 链表
题目：判断是否有环——快慢指针
https://leetcode-cn.com/problems/linked-list-cycle/solution/kuai-man-zhi-zhen-fa-dai-ma-zhong-zhu-sh-cdst/
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow = head # 慢指针
        fast = head # 快指针
        # while p1 and p2:
        while fast and fast.next:
            # 为什么这样判断可以？？
            # p2.next只是为了p2.next.next不报错
            slow = slow.next
            fast = fast.next.next
            # 如何判断遇见两次了呢？已解
            if slow == fast:
                return True
        return False

if __name__ == '__main__':
    a = ListNode(3)
    b = ListNode(2)
    # c = ListNode(0)
    # d = ListNode(-4)
    a.next = b
    b.next = a
    # c.next = d
    # d.next = b
    print(Solution().hasCycle(a))