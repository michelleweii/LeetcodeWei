"""
easy 2021-11-04 快慢指针
https://leetcode-cn.com/problems/middle-of-the-linked-list/solution/kuai-man-zhi-zhen-zhu-yao-zai-yu-diao-shi-by-liwei/
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode(self, head):
        if not head:return head
        slow, fast = head, head # 奇怪，这里和148不一样，148要fast=head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow

    def middleNode_ori(self, head):
        cur = head
        count = 1
        while cur != None:
            count += 1
            cur = cur.next
        mid = (count-1) // 2 + 1
        point = 1
        cur = head
        if mid == 1:
            return head
        while cur != None:
            if point != mid:
                point += 1
                cur = cur.next
            else:
                return cur

if __name__ == '__main__':
    head = [1,2,3,4,5]