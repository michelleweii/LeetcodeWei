"""
middle 链表
2021-07-16
估计代码太长了，面试不会考
拼接 + 拆分
https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/solution/jian-zhi-offer-35-fu-za-lian-biao-de-fu-zhi-ha-xi-/
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        if not head: return head
        cur = head
        # 1. 复制各节点，并构建拼接链表
        while cur:
            fake = Node(cur.val)
            fake.next = cur.next
            cur.next = fake
            cur = fake.next
            # 成z字

        # 2. 构建各新节点的 random 指向
        p = head
        while p:
            # 注意这里有random节点才改变
            if p.random:
                p.next.random = p.random.next
            p = p.next.next

        # 3. 拆分两链表
        pre = head # 指向旧链表
        cur = head.next # 指向新链表
        res = head.next # 指向新链表
        while cur.next:
            pre.next = pre.next.next # 删除旧与新的连接
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        # pre.next = None  # 单独处理原链表尾节点
        return res


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n1.next = n2
    n1.random = n2
    n2.next = None
    n2.random = n1
    print(Solution().copyRandomList(n1))