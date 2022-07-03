"""
middle 2021-11-08 链表反向双指针
https://leetcode-cn.com/problems/reorder-list/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-34/
(这个思路)https://leetcode-cn.com/problems/reorder-list/solution/dong-hua-yan-shi-kuai-man-zhi-zhen-143-z-4kmk/
重排链表=LC876.链表的中间节点+LC206.反转链表
    # 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
    # 通过观察给到的示例，其结果是将原链表的前半部分和原链表的后半部分反转之后的链表进行合并得到的。
因此，整体思路就是：
首先，找到链表的中间节点，方法如上述的#86题；
接着，将链表的后半部分反转，放入如上述的#206题；
然后，将链表的前半部分和链表的后半部分反转后的结果进行合并。
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # LC876 链表的中间节点
    def get_middle(self, head):
        if not head or not head.next: return head
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        # mid = slow
        return slow

    # LC206.反转链表
    def reverse_list(self, head):
        if not head or not head.next: return head
        pre, cur = None, head
        while cur:
            tail = cur.next
            cur.next = pre
            pre = cur
            cur = tail
        return pre

    # LC143.重排链表
    def reorderList(self, head):
        # if not head or not head.next: return head
        # 获得中间节点
        mid = self.get_middle(head)
        # print(mid.val)
        # 中间节点之后的部分进行反转
        head2 = mid.next
        mid.next = None
        head2 = self.reverse_list(head2) # 5,4
        # print(head2.val)
        # 合并
        head1 = head # 1,2,3
        while head1 and head2:
            next1, next2 = head1.next, head2.next
            head1.next = head2
            head1 = next1
            head2.next = head1
            head2 = next2
        # return head

    # def reorderList2store(self, head: ListNode) -> None:
    #     if not head or not head.next:return
    #     p = head
    #     linklist = []
    #     # 将链表值存到 list 中, list=[1,2,3,4]
    #     while p:
    #         linklist.append(p)
    #         p = p.next
    #     # print(linklist) # [<__main__.ListNode object at 0x7f9f5f70e2d0>, <__main__.ListNode object at 0x7f9f5f727610>, <__main__.ListNode object at 0x7f9f5f72b350>, <__main__.ListNode object at 0x7f9f5f72dc50>]
    #     # for i in linklist:
    #     #     self.print_node(i)
    #     # 头尾指针依次取元素
    #     i, j = 0, len(linklist)-1
    #     while i<j:
    #         linklist[i].next = linklist[j]
    #         # for i in linklist:
    #         #     self.print_node(i)
    #         i += 1
    #         # 偶数个节点的情况，会提前相遇
    #         if i == j:break
    #         linklist[j].next = linklist[i]
    #         j -= 1
    #     linklist[i].next = None
    #
    # def myprint(self, head):
    #     res = []
    #     while head:
    #         res.append(head.val)
    #         head = head.next
    #     print("list:", res)

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    a.next = b
    b.next = c
    c.next = d
    print(Solution().reorderList(a))