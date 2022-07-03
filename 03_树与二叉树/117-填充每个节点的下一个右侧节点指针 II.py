"""
middle 2021-12-28 层次遍历
https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/solution/bfsjie-jue-zui-hao-de-ji-bai-liao-100de-yong-hu-by/
题目：与LC116不同(完美二叉树)，本题为二叉树。
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    # bfs 时间复杂度O(N), 空间复杂度O(N)
    def bfs(self, root):
        if not root:return root
        q, res = [root], []
        while q:
            # cur_level = []
            size = len(q) # 每一层的数量
            pre = None # 前一个节点，标记是否有元素
            for i in range(size):
                node = q.pop(0) # 出队
                # 如果pre为空就表示node节点是这一行的第一个
                # 没有前一个节点指向他，否则就让前一个节点指向他
                if pre is not None:
                    pre.next = node
                # 然后再让当前节点成为前一个节点
                pre = node
                # 左右子节点如果不为空就入队
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # res.append(cur_level[:])
        # return res
        return root

    # 每层单链表法 时间复杂度O(N), 空间复杂度O(1)
    # 每一行都可以看成一个链表比如第一行就是只有一个节点的链表，
    # 第二行是只有两个节点的链表（假如根节点的左右两个子节点都不为空）……
    def connect(self, root):
        if root is None: return root
        first = root
        while first: # 如果树不为null
            head = tail = Node(0)
            cur = first
            while cur:  # 遍历当前层
                if cur.left:
                    tail.next = cur.left
                    tail = tail.next
                if cur.right:
                    tail.next = cur.right
                    tail = tail.next
                cur = cur.next
            first = head.next
        return root

if __name__ == '__main__':
    a = Node(1)

