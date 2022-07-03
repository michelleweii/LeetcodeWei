"""
middle 2021-10-15 链表
# 思路一：将两个逆序链表转为list，转为数字后，相加。求和之后的数字再转为linknode
# 思路二：https://leetcode-cn.com/problems/add-two-numbers/solution/hua-jie-suan-fa-2-liang-shu-xiang-jia-by-guanpengc/
和字符串相加差不多，两数求和也是从后向前计算，符合逆序
"""
# 2021-12-21
from functools import reduce
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 思路二
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(-1)
        cur = dummy
        carry = 0 # 进位
        while l1 is not None or l2 is not None:
            # 将两个链表看成是相同长度的进行遍历，如果一个链表较短则在前面补 0，
            # 比如 987 + 23 = 987 + 023 = 1010
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            sum = x+y+carry

            carry = sum // 10
            sum = sum % 10
            cur.next = ListNode(sum)
            cur = cur.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        # 如果两个链表全部遍历完毕后，进位值为 1，
        # 则在新链表最前方添加节点 1
        if carry==1:
            cur.next = ListNode(carry)

        return dummy.next


    # 思路一
    def addTwoNumbers_1(self, l1, l2):
        sums = self.convertNum(l1)+self.convertNum(l2)
        sums = list(map(int, str(sums)))[::-1] # 807->[8, 0, 7]
        p = ListNode(-1)
        head = p
        for x in sums:
            node = ListNode(x)
            p.next = node
            p = p.next
        return head.next

    def convertNum(self, node):
        nums = []
        while node:
            nums.append(node.val)
            node = node.next
        # 将[2,4,3]转为[3,4,2]
        nums = nums[::-1]
        combine = reduce((lambda nums,y : nums*10+y), nums)
        return combine


if __name__ == '__main__':
    l1 = ListNode(2)
    a = ListNode(4)
    b = ListNode(3)
    l1.next = a
    a.next = b
    l2 = ListNode(5)
    c = ListNode(6)
    d = ListNode(4)
    l2.next = c
    c.next = d
    print(Solution().addTwoNumbers(l1,l2))