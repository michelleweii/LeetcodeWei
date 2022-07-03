"""
middle 2021-12-21 链表
题目：位置奇数节点+位置偶数节点
https://leetcode-cn.com/problems/odd-even-linked-list/solution/shou-hua-tu-jie-328qi-ou-lian-biao-odd-even-linked/
odd 指针扫描奇数结点，even 指针扫描偶数结点
3个指针（扫描奇数结点、扫描偶数结点、保存偶链的头结点）
"""
# 类似lc86
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:return head

        odd = head # 扫描奇数结点
        even = head.next # 扫描偶数结点
        even_head = even # 保存偶链的头结点

        while even is not None and even.next is not None:
            odd.next = even.next # even.next是下一个奇数节点
            odd = odd.next # odd 推进到下一个奇数节点
            even.next = odd.next # 下一个奇数节点的next是下一个偶数节点
            even = even.next # even推进到下一个偶数节点

        odd.next = even_head # 奇链连上偶链
        return head


    def print_list(self, head):
        while head:
            print(head.val)
            head = head.next

if __name__ == '__main__':
    a = ListNode(2)
    b = ListNode(1)
    c = ListNode(3)
    d = ListNode(5)
    e = ListNode(6)
    f = ListNode(4)
    g = ListNode(7)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g
    res = Solution().oddEvenList(a)
    Solution().print_list(res)