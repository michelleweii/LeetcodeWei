"""
hard 2021-12-21 链表（优先队列）超级常考
【归并，分治】https://leetcode-cn.com/problems/merge-k-sorted-lists/solution/leetcode-23-he-bing-kge-pai-xu-lian-biao-by-powcai/
代码看注释部分的
"""
# 思路一：先把整个链表拉成一个链表，把这个链表的值全部存储在列表中，再将列表排序，新建一个链表重新一个一个指向列表的每一项
# 优先队列:nlogk, n 是所有链表中元素的总和，k 是链表个数。

# 思路二：分治——>归并
# https://leetcode-cn.com/problems/merge-k-sorted-lists/solution/python-23he-bing-kge-sheng-xu-lian-biao-ep54a/
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1(object):
    # 使用分治思想：把2个list当做已经排序好的，准备进行归并的两个数组
    def mergeKLists(self, lists):
        if not lists: return
        """
        将链表list中的链表两两合并改为->归并合并。好难理解哦
        """
        return self.merge_sort(lists, 0, len(lists)-1) # 记录子链表数量

    # 归并排序 [l,mid]+[mid+1,r]
    def merge_sort(self, lists, l, r):
        if l >= r:
            return lists[l] # 链表头节点
        mid = (l+r)//2
        l1 = self.merge_sort(lists, l, mid)
        l2 = self.merge_sort(lists, mid+1, r)
        return self.merge_two_lists(l1, l2)

    # 链表归并，两个链表【合并】成有序
    def merge_two_lists(self, l1, l2):
        p = head = ListNode(-1)
        while l1 and l2:
            if l1.val<l2.val:
                p.next,l1 = l1, l1.next
            else:
                p.next,l2 = l2,l2.next
            p = p.next
        if l1: p.next = l1
        if l2: p.next = l2
        return head.next

# """
#         if not lists: return
#         """
#         # 将链表list中的链表两两合并改为 归并合并
#         # 好难理解哦
#         """
#         n = len(lists)
#         return self.merge_sort(lists, 0, n-1) # 记录子链表数量
#
#     # 归并排序 [l,mid]+[mid+1,r]
#     def merge_sort(self, lists, l, r):
#         if l >= r:
#             return lists[l]
#         mid = (l+r)//2
#         l1 = self.merge_sort(lists, l, mid)
#         l2 = self.merge_sort(lists, mid+1, r)
#         #
#         p = head = ListNode(-1)
#         while l1 and l2:
#             if l1.val<l2.val:
#                 p.next,l1 = l1, l1.next
#             else:
#                 p.next,l2 = l2,l2.next
#             p = p.next
#         if l1: p.next = l1
#         if l2: p.next = l2
#         return head.next
#
# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         import heapq #调用堆
#         minHeap = []
#         for listi in lists:
#             while listi:
#                 heapq.heappush(minHeap, listi.val) #把listi中的数据逐个加到堆中
#                 listi = listi.next
#         dummy = ListNode(0) #构造虚节点
#         p = dummy
#         while minHeap:
#             p.next = ListNode(heapq.heappop(minHeap)) #依次弹出最小堆的数据
#             p = p.next
#         return dummy.next
# """

from queue import PriorityQueue # 方法一
from heapq import heappush, heappop # 方法二
class Solution2(object):
    # 优先队列
    def mergeKLists_q(self, lists):
        dummy = curr = ListNode(None)
        q = PriorityQueue() # 定义优先队列
        for idx,node in enumerate(lists):
            # 我的妈，链表竟然可以这样遍历
            # print(idx,node) # TypeError: 'ListNode' object is not iterable
            # 不可以这样遍历- -
            if node:
                # print((node.val, idx, node))
                # (1, 0, <__main__.ListNode object at 0x7ffd835f3210>)
                # (1, 1, <__main__.ListNode object at 0x7ffd83613950>)
                # (2, 2, <__main__.ListNode object at 0x7ffd86d29d50>)
                q.put((node.val, idx, node))
        # print(q.get()) # (1, 0, <__main__.ListNode object at 0x105d20518>)
        # 如果优先队列不为空
        while not q.empty():
            # 最小的元素在链表尾部
            value, idx, curr.next = q.get() # 弹出来的是小的数，升序, [1,1,2]
            curr = curr.next
            if curr.next:
                q.put((curr.next.val, idx, curr.next))
        return dummy.next

    ## using minheap
    ## 小根堆
    def mergeKLists2(self, lists):
        dummy = curr = ListNode(None)
        heap = []
        for idx, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, idx, node))

        while heap:
            _, idx, curr.next = heappop(heap)
            curr = curr.next
            if curr.next:
                heappush(heap, (curr.next.val, idx, curr.next))
        return dummy.next

if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(4)
    c = ListNode(5)

    d = ListNode(1)
    e = ListNode(3)
    f = ListNode(4)

    g = ListNode(2)
    h = ListNode(6)

    a.next = b
    b.next = c
    d.next = e
    e.next = f
    g.next = h

    lists = [a,d,g]
    print(Solution1().mergeKLists(lists))
