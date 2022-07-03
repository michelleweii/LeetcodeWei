"""
middle 2021-10-15 链表【字节】
指定区间反转链表
【头插法】https://leetcode-cn.com/problems/reverse-linked-list-ii/solution/java-shuang-zhi-zhen-tou-cha-fa-by-mu-yi-cheng-zho/
"""
# 2021-12-22
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 2021/12/22
    def reverseBetween(self, head, m, n):
        # 定义一个dummyHead, 方便处理
        dummy = ListNode(-1)
        dummy.next = head
        g = dummy
        p = dummy.next
        # 将指针移到相应的位置
        for _ in range(m-1):
            g = g.next # 将 g 移动到第一个要反转的节点的前面
            p = p.next # 将 p 移动到第一个要反转的节点的位置上

        # 头插法插入节点
        # 将 p 后面的元素删除，然后添加到 g 的后面。也即头插法
        for i in range(n-m):
            removed = p.next
            p.next = removed.next # 可以p.next.next

            removed.next = g.next # 不能换成p
            g.next = removed
        return dummy.next

    # 2020/12/25
    def reverseBetween_old(self, head: ListNode, m: int, n: int):# -> ListNode:
        if head is None: return head
        pre = None
        cur = head
        i = 1
        while i < m and cur != None:
            # 其实标记一个变量的方法，对我来说可能更好理解
            pre = cur
            cur = cur.next
            # cur指向的是m所在的节点
            i += 1

        # 要记录开始反转的节点的前一个，因为要连接变换后的节点
        t1 = pre
        # 要记录开始反转的节点，因为要连接剩余的节点
        t2 = cur
        while (i <= n and cur != None):
            rear = cur.next
            cur.next = pre
            pre = cur
            cur = rear
            i += 1

        if m == 1:
            t2.next = cur # 此时cur为none，原头结点指向node
            return pre # pre目前在原链表的末尾

        t2.next = cur
        t1.next = pre
        return head

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
    print(Solution().reverseBetween(a,2,4))