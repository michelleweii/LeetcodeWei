"""
middle 2021-11-08 链表（快慢指针）
要求：将链表每个节点向右移动 k 个位置
https://leetcode-cn.com/problems/rotate-list/solution/java-shuang-zhi-zhen-100-by-programmery-31h5/
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head, k):
        if not head or not k: return head
        # 求链表长度，k有可能大于链表长度，所以首先获取一下链表长度len。
        # 如果k % len == 0，等于不用旋转，直接返回头结点
        h, length = head, 0
        while h: h, length = h.next, length + 1
        if k%length==0:return head

        slow, fast = head, head

        # 快指针先走k步，注意这里是求余，因为k可能会比length大好几倍
        while k%length>0:
            fast = fast.next
            k -= 1

        # 注意这里fast指向链表最后一个节点，所以要fast.next=None
        # 否则就是fast = None
        while fast.next:
            slow, fast = slow.next, fast.next

        # 快指针走到链表尾部时，慢指针刚好走到结果链表的尾部。
        res = slow.next
        slow.next = None  # 慢指针指向的节点断开和下一节点的联系
        fast.next = head  # 最后一个节点将之前的head接到后面

        return res

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    k = 2
    print(Solution().rotateRight(a,k))