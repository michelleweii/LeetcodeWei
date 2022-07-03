"""
easy 2021-12-24 链表找中点+反转链表
# 要求时间复杂度为O(n)，空间复杂度为O(1)
（结构清晰点）https://leetcode-cn.com/problems/palindrome-linked-list/solution/hui-wen-lian-biao-mo-ban-zong-jie-jian-y-dzen/
https://leetcode-cn.com/problems/palindrome-linked-list/solution/234-hui-wen-lian-biao-kuai-man-zhi-zhen-mjtur/

字符串判断回文串？
思路：
1、找中点
2、翻转一半
3、2个链表逐个比较节点val是否相同
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        mid = self.get_mid(head)
        head2 = mid.next # 要跳过中点
        mid.next = None # 断开前半部分两边
        head2 = self.reverse_list(head2) # 反转后半部分链表
        head1 = head
        # 开始对比
        while head1 and head2:
            if head1.val != head2.val:return False
            head1, head2 = head1.next, head2.next

        return True

    def reverse_list(self, head):
        pre = None
        cur = head
        while cur:
            tail = cur.next
            cur.next = pre
            pre = cur
            cur = tail
        return pre

    # 快慢指针求链表中点
    def get_mid(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # mid = slow
        return slow

    # """
    # 存储为array之后再反转对比
    # """
    # def isPalindrome_old(self, head):
    #     listNode = []
    #     cur = head
    #     while cur:
    #         listNode.append(cur.val)
    #         cur = cur.next
    #     if len(listNode) == 0:
    #         return True
    #     curList = listNode[::-1]
    #     return curList == listNode

if __name__ == '__main__':
    # head = [1,2]
    a = ListNode(1)
    b = ListNode(2)
    a.next = b
    print(Solution().isPalindrome(a))