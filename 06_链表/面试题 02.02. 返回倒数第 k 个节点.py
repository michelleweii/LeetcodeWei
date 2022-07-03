"""
easy 2021-12-23 双指针一次遍历
https://leetcode-cn.com/problems/kth-node-from-end-of-list-lcci/solution/shuang-zhi-zhen-zhan-di-gui-3chong-jie-jue-fang-2/
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        p1, p2 = head, head
        while k and p2:
            p2 = p2.next
            k -= 1

        while p1 and p2:
            p1, p2 = p1.next, p2.next

        return p1.val

if __name__ == '__main__':
    pass