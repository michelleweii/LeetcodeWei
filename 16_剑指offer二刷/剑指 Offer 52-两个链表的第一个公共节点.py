"""
easy 链表
https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/solution/shuang-zhi-zhen-fa-lang-man-xiang-yu-by-ml-zimingm/
2021-07-18
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pa, pb = headA, headB
        while pa!=pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa


if __name__ == '__main__':
    a = ListNode(2)
    b = ListNode(1)
    c = ListNode(6)
    d = ListNode(4)
    e = ListNode(5)
    a.next = c
    c.next = d
    b.next = e
    # listA = [2, 6, 4], listB = [1, 5]
    print(Solution().getIntersectionNode(a, b))