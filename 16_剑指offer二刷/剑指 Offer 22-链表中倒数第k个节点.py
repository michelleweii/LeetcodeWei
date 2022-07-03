"""
easy 链表
2021-07-14
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        p = head
        lens = 0
        while p:
            lens += 1
            p = p.next

        n = lens - k + 1
        p = head
        for i in range(1, n):
            p = p.next
        return p

if __name__ == '__main__':
    head = [1, 2, 3,4, 5]
    k = 2
    print(Solution().getKthFromEnd(head, k))