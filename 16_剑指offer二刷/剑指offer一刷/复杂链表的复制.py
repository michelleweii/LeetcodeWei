# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:return None
        p = pHead
        # 完成节点复制
        while p:
            node = RandomListNode(p.label)
            tail = p.next
            p.next = node
            node.next=tail
            p = tail
        # 复制随机指针
        q = pHead
        while q:
            if q.random:
                q.next.random = q.random.next
            q = q.next
        # 开始连接复制的节点
        cloNode = pHead
        pHead = pHead.next
        while cloNode.next:
            node = cloNode.next
            cloNode.next = node.next
            cloNode = node
        return pHead


if __name__ == '__main__':
    a = RandomListNode(1)
    b = RandomListNode(2)
    c = RandomListNode(3)
    d = RandomListNode(4)
    e = RandomListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    a.random = e
    print(Solution().Clone(a))