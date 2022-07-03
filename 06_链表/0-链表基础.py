
# 链表求中点
def get_mid(head):
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next  ### 注意，mid是slow的next，而不是最终的停止点！
    slow.next = None

