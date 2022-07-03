"""
hard 2021-10-13 高频题（必会）
[递归，好理解]https://leetcode.cn/problems/reverse-nodes-in-k-group/solution/di-gui-java-by-reedfan-2/
https://leetcode-cn.com/problems/reverse-nodes-in-k-group/solution/tu-jie-kge-yi-zu-fan-zhuan-lian-biao-by-user7208t/
1、链表分区为已翻转部分+待翻转部分+未翻转部分
2、每次翻转前，要确定翻转链表的范围，这个必须通过 k 此循环来确定
3、【需记录翻转链表前驱和后继，方便翻转完成后把已翻转部分和未翻转部分连接起来】
4、【初始需要两个变量 pre 和 end，pre 代表待翻转链表的前驱，end 代表待翻转链表的末尾】注意是待翻转
5、经过k此循环，end 到达末尾，记录待翻转链表的后继 next = end.next
6、翻转链表，然后将三部分链表连接起来，然后重置 pre 和 end 指针，然后进入下一次循环
7、特殊情况，当翻转部分长度不足 k 时，在定位 end 完成后，end==null，已经到达末尾，说明题目已完成，直接返回即可
8、时间复杂度为 O(n*K)最好的情况为O(n) 最差的情况未 O(n^2)
9、空间复杂度为 O(1)除了几个必须的节点指针外，我们并没有占用其他空间
"""
# 需要4个指针，pre->start->end->post；
# pre：待翻转区前一个；指向已翻转最后一个；
# start：待翻转区开始；
# end：待翻转区结束；
# post：待翻转区后一个；指向未翻转第一个；
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 递归(简单) 空间复杂度应该是O(n)
    # https://leetcode.cn/problems/reverse-nodes-in-k-group/solution/di-gui-java-by-reedfan-2/
    def reverseKGroup_pro(self,head,k): #ListNode, k: int) -> ListNode:
        if not head or not head.next:return head
        tail=head
        for i in range(k):
            if tail==None:return head # 剩余数量小于k的话，则不需要反转。
            tail=tail.next
        # 翻转前k个元素
        newhead=self.reverse(head,tail)
        # 下一轮的开始的地方就是tail
        head.next=self.reverseKGroup_pro(tail,k) # head.next=newhead, head=3,newhead=5
        return newhead

    def reverse(self,head,tail):
        prev=None
        while head!=tail:
            t=head.next
            head.next=prev
            prev=head
            head=t
        return prev

    # ### 繁琐的迭代，考虑边界太多
    # https://leetcode.cn/problems/reverse-nodes-in-k-group/solution/tu-jie-kge-yi-zu-fan-zhuan-lian-biao-by-user7208t/
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:return head
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy  # 待翻转区前一个；指向已翻转最后一个；
        start = end = post = head
        # start = head # 待翻转区开始；
        # end = head # 待翻转区结束；
        # post = head # 待翻转区后一个；指向未翻转第一个；
        while post: # post代表有下一个新的开始
            # 据k找到end 注意链表是否结束
            for i in range(1, k): # 注意要从1开始
                if end: end = end.next
            # 如果链表的尾部没有被k整除, 跳出while循环
            # 不满足k个一组的翻转条件，剩余节点保持原有顺序
            if end is None: break
            # 对翻转区进行翻转
            post = end.next
            end.next = None # 断开与原链表的连接
            end = start # 这里第一次不明白，注意!
            start = self.reverse206(start) # 这里，end-start的关系注意！
            # 与原链表接上
            end.next = post
            pre.next = start #2

            # 重新指定pre，start，end
            pre = end
            start=end=post # 从开始位置继续找k个
        return dummy.next

    def reverse206(self, head):
        """
        lc206.反转链表，翻转整个以head为头的链表
        翻转链表需要3个指针
        """
        pre = None
        cur = head
        while cur:
            post = cur.next
            cur.next = pre
            pre = cur
            cur = post
        # 返回新的链表头部
        return pre

if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    k = 2
    print(Solution().reverseKGroup(n1, k))