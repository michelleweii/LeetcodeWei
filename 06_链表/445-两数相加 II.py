"""
middle 2021-12-23 链表/栈
对比lc2，本题要求不能反转链表
https://leetcode-cn.com/problems/add-two-numbers-ii/solution/fu-xue-ming-zhu-xiang-jie-qiu-jia-fa-xue-ofb5/
思路：
1、两个链表节点入栈
2、弹栈+计算+头插（此步骤需要引入新的节点）
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stk1, stk2 = [], []
        while l1:
            stk1.append(l1.val)
            l1 = l1.next
        while l2:
            stk2.append(l2.val)
            l2 = l2.next
        dummy = ListNode(-1)
        carry = 0 # 进位
        # print(stk1, stk2)
        while stk1 or stk2:
            x = stk1.pop() if stk1 else 0
            y = stk2.pop() if stk2 else 0
            sum = x+y+carry

            carry = sum//10
            sum = sum%10

            cur = ListNode(sum)
            # 链表在插入的时候如何进行反转？头插法
            cur.next = dummy.next
            dummy.next = cur

        if carry==1:
            cur = ListNode(carry)
            cur.next = dummy.next
            dummy.next = cur

        return dummy.next

if __name__ == '__main__':
    # l1 = [7, 2, 4, 3], l2 = [5, 6, 4]
    # [7,8,0,7]
    l1 = ListNode(7)
    a = ListNode(2)
    b = ListNode(4)
    c = ListNode(3)
    l1.next, a.next, b.next = a, b, c
    l2 = ListNode(5)
    d = ListNode(6)
    e = ListNode(4)
    l2.next, d.next = d, e
    print(Solution().addTwoNumbers(l1,l2))