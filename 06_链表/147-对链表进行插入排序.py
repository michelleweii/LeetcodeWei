"""
middle 2021-11-02 插入排序（链表）
https://leetcode-cn.com/problems/insertion-sort-list/solution/147-dui-lian-biao-jin-xing-cha-ru-pai-xu-3uc3/
利用直接插入排序的算法思想，单链表无法向前遍历，需要通过三个指针完成操作。
这个动图很容易理解：https://leetcode-cn.com/problems/insertion-sort-list/solution/dong-hua-mo-ni-fei-chang-jian-ji-by-chef-bg3d/
建1个dummy，每来一个元素，就从dummy开始遍历，如果dummy.next<cur，dummy++
否则，cur插入到dummy和dummy.next之间。
"""
# 思路：
# 给cur找到一个合适的位置！！！
# 明确出步骤： 先找它cur - 临时保存它 - 删掉它 - 给它找位置 - 插入它
# 插入要先改 temp.Next，再接到 prev 的后面，而不是先接到 prev 后面，再改 temp.Next，这样会丢失 prev.Next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head):
        # 解答代码还是看的官方题解
        if not head: return head
        dummy = ListNode(-1)
        dummy.next = head
        # cur负责指向新元素，pre负责指向新元素的前一元素
        # 判断是否需要执行插入操作
        curr = head.next # pos # 给cur找到一个合适的位置
        pre = head
        while curr:
            # 不需要插入到合适的位置，则继续向下移动
            if pre.val <= curr.val:
                pre = pre.next
            else:
                # 每次从起点出发，查找新元素的合适位置。时间复杂度O(N^2)
                temphead = dummy
                while temphead.next.val<=curr.val:
                    temphead = temphead.next

                # 已经找到了合适位置，我们需要进行插入
                pre.next = curr.next
                curr.next = temphead.next
                temphead.next = curr
            curr = pre.next

        return dummy.next

if __name__ == '__main__':
    a = ListNode(4)
    b = ListNode(2)
    c = ListNode(1)
    d = ListNode(3)
    a.next = b
    b.next = c
    c.next = d
    print(Solution().insertionSortList(a))
