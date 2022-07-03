"""
easy 2021-12-23 链表
题目：判断链表相交位置——双指针
https://leetcode-cn.com/problems/intersection-of-two-linked-lists/solution/intersection-of-two-linked-lists-shuang-zhi-zhen-l/
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 双指针解法 2021/12/23
    def double_pointer(self, headA, headB):
        if (not headA or not headB):
            return None
        # 定义两个指针, 第一轮让两个到达末尾的节点指向另一个链表的头部, 最后如果相遇则为交点(在第一轮移动中恰好抹除了长度差)
        # 两个指针等于移动了相同的距离, 有交点就返回, 无交点就是各走了两条指针的长度
        pA = headA
        pB = headB
        # 在这里第一轮体现在pA和pB第一次到达尾部会移向另一链表的表头, 而第二轮体现在如果pA或pB相交就返回交点, 不相交最后就是null == null
        while pA != pB:
            pA = pA.next if pA else headB # a+c+b
            pB = pB.next if pB else headA # b+c+a
        return pA

    # 2020/12/25
    def getIntersectionNode(self, headA, headB):
        lenA, lenB = 0, 0
        pA = headA
        pB = headB
        while pA:
            pA = pA.next
            lenA += 1
        while pB:
            pB = pB.next
            lenB += 1
        pA = headA
        pB = headB
        if lenA > lenB:
            for i in range(lenA - lenB):
                pA = pA.next
        else:
            for i in range(lenB - lenA):
                pB = pB.next
        while pA != pB:
            pA = pA.next
            pB = pB.next
        return pA

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next = b
    b.next = c
    d = ListNode(4)
    e = ListNode(5)
    f = ListNode(6)
    d.next = e
    e.next = f
    f.next = b
    print(Solution().getIntersectionNode(a,d))