
# 2022-02-28

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        if not lists: return
        n = len(lists)
        return self.merge_sort(lists, 0, n - 1)

    # # 原来归并的是数字，现在归并的是list
    def merge_sort(self, lists, l, r):
        if l >= r: return lists[l]
        mid = l + (r - l) // 2
        l1 = self.merge_sort(lists, l, mid)
        l2 = self.merge_sort(lists, mid + 1, r)

        d = dummy = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                d.next, l1 = l1, l1.next
            else:
                d.next, l2 = l2, l2.next
            d = d.next
        d.next = l1 if l1 else l2
        return dummy.next

if __name__ == '__main__':
    a=ListNode(1)
    b=ListNode(4)
    c=ListNode(5)
    a.next=b
    b.next=c

    d=ListNode(1)
    e=ListNode(3)
    f=ListNode(4)
    d.next=e
    e.next=f

    g=ListNode(2)
    h=ListNode(6)
    g.next=h

    res = [[a],[d],[g]]

    print(Solution().mergeKLists(res))
