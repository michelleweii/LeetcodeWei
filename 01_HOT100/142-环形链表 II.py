"""
middle 2021-12-23 链表
题目：判断环链表的入口位置——快慢指针
（推导+动图）https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/linked-list-cycle-ii-kuai-man-zhi-zhen-shuang-zhi-/
"""
# a：起点到环入口的节点数（不包括入口）
# b：环节点数
# 根据： f=2s （快指针每次2步，路程刚好2倍）
# f=s+nb (相遇时，刚好多走了n圈), =>推出：s = nb。
# 从head结点走到入环点需要走：a+nb, 而slow已经走了nb，那么slow再走a步就是入环点了。
# (如果让指针从链表头部一直向前走并统计步数k，那么所有 走到链表入口节点时的步数 是：k=a+nb（先走a步到入口节点，之后每绕1圈环（ b步）都会再次到入口节点）。)
# 如何知道slow刚好走了a步？ 从head开始，和fast指针一起走，相遇时刚好就是a步。
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 方法二：# 掌握推导过程
    # 2022/02/28更新
    """
    假设a是head至环入口长度，b是环长度，假设fast一共走了K=a+nb;
    有 f=2s, f=s+nb (相遇时，刚好多走了n圈), =>推出：s = nb。
    =》fast = a+s，相遇时，s再走a即到达入口。
    =》slow如何再走a? fast回到起始点head，走a，slow也走a，即两者再次相遇是环入口位置。
    """
    def detectCycle(self, head: ListNode) -> ListNode:
        # 链表相遇位置到环入口的距离
        #=从链表开始到环入口的距离
        # 1.求相遇点(使用快慢指针)
        if not head or not head.next:return None
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:break # 停在了相遇节点
        if slow!=fast:
            return None # 如果链表不存在环

        fast = head # 再从head出发，走a个节点
        while fast!=slow:
            fast = fast.next
            slow = slow.next
        return fast

    # 方法一：
    # 环入口怎么求？
    # 快慢指针的相遇点到环入口的距离 == 链表起始点到环入口的距离
    def detectCycle_old(self, head):
        p1 = head   # 慢指针
        p2 = head   # 快指针
        encounter = head
        flag = 0
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                # 相遇点
                encounter = p1
                flag = 1
                break
        if not flag:
            return None

        # print(encounter.val) # -4
        start = head
        pos = 0
        while start and encounter:
            if start == encounter:
                pos += 1
                # return pos # # 返回相遇节点的位置
                return start # 返回相遇点(ac)
            start = start.next
            encounter = encounter.next
        # return -1 # 返回相遇节点的位置
        return None

if __name__ == '__main__':
    a = ListNode(3)
    b = ListNode(2)
    c = ListNode(0)
    d = ListNode(-4)
    a.next = b
    b.next = c
    c.next = d
    d.next = b
    print(Solution().detectCycle(a))