"""
middle 2021-12-28 层次遍历
https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/solution/dong-hua-yan-shi-san-chong-shi-xian-116-tian-chong/
"""
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def bfs(self, root):
        if not root:return root
        q, res = [root], []
        while q:
            # cur_level = []
            size = len(q)
            # 新添加，将队列中的元素串联起来
            node = q[0]
            for i in range(1, size):
                node.next = q[i]
                node = q[i]
            # 遍历队列中的每个元素，将每个元素的左右节点也放入队列中
            for i in range(size):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # res.append(cur_level[:])
        # return res
        return root

    def connect(self, root):
        def dfs(root):
            if not root:
                return
            left = root.left
            right = root.right
            # 配合动画演示理解这段，以root为起点，将整个纵深这段串联起来
            while left:
                left.next = right
                left = left.right
                right = right.left
            # 递归的调用左右节点，完成同样的纵深串联
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return root

if __name__ == '__main__':
    pass

