"""
easy 2021-12-24
题目: 只能直接访问要被删除的node节点
思路：用后续节点来覆盖要被删除的节点
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 2020/12/25
    def deleteNode(self, node):
        # 只有对要删除节点node的访问权限
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 题目给的是删除节点，那说明这个节点可以舍弃了，我们把下一个节点的值拷贝
        # 给当前要删除的节点，再删除下一个节点。
        node.val = node.next.val
        node.next = node.next.next

# class SingleList(object):
def strToListNode(input):
    """将list转为链表"""
    numbers = input
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next
    ptr = dummyRoot.next
    return ptr

def travel(input):
    """打印链表"""
    cur = input
    while cur != None:
        print(cur.val, end=' ')
        cur = cur.next
    print("")

if __name__ == '__main__':
    head = [4,5,1,9,5]
    node = 5
    ptr = strToListNode(head)
    travel(ptr)
    ans = Solution()
