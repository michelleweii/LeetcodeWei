"""
middle 2020/12/25 链表（双指针）
一次遍历解决问题：两个指针间距n，当后一个指针移动到末尾node(while p2.next)，前一个指针就落在要删除的前一个节点了
https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/solution/dong-hua-tu-jie-leetcode-di-19-hao-wen-ti-shan-chu/
"""
# 2021-12-21
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 双指针 2020/12/25
    # 一次遍历解决问题
    def removeNthFromEnd(self, head, n):
        if not head:return head
        dummy = ListNode(0)
        dummy.next = head
        p1 = p2 = dummy
        for i in range(n):
            p2 = p2.next # 后一个指针
            # print(i, p2.val) # 1 2
        while p2.next: # 停在最后一个节点
            p1 = p1.next # 前一个指针
            p2 = p2.next
        p1.next = p1.next.next
        return dummy.next

    # 两次遍历，先求移动长度n-k，再遍历链表删除节点
    def removeNthFromEnd2(self, head, n):
        lenLink = self.length(head)
        print(lenLink)
        changed = lenLink-n
        cur = head
        pos = 1
        if changed == 0:
            head = head.next
            # self.printList(head)
            return head
        else:
            while cur and pos!=changed:
                rear = cur.next
                pos+=1
                cur = cur.next
            rear = cur.next
            cur.next = rear.next
            rear.next = None
            return head
            # self.printList(head)

    # 打印链表
    def printList(self,head):
        while head:
            print(head.val,end='->')
            head = head.next
        print()

    # 求链表长度
    def length(self,head):
        if head is None:
            return 0
        cnt = 0
        cur = head
        while cur:
            cur = cur.next
            cnt+=1
        return cnt

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
    n = 2
    print(Solution().removeNthFromEnd(a,n))
