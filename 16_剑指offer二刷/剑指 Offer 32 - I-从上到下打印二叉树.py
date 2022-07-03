"""
middle 二叉树
2021-07-15
32题 i ii iii如下：
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # [3,9,20,15,7]
    def levelOrder1(self, root):
        if not root:return []
        queue = []
        res = []
        queue.append(root)
        while queue:
            tmp = queue.pop(0)
            res.append(tmp.val)
            if tmp.left:
                queue.append(tmp.left)
            if tmp.right:
                queue.append(tmp.right)
        return res

    # [[3], [9,20], [15,7]]
    def levelOrder2(self, root):
        if not root:return []
        queue = []
        res = []
        queue.append(root)
        while queue:
            cur_level, size = [], len(queue)
            for i in range(size):
                tmp = queue.pop(0)
                cur_level.append(tmp.val)
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
            res.append(cur_level[:])
        return res

    # 之字形遍历
    # [[3], [20,9], [15,7]]
    def levelOrder3(self, root):
        if not root:return []
        queue = []
        res = []
        queue.append(root)
        flag = 1
        while queue:
            cur_level, size = [], len(queue)
            for i in range(size):
                tmp = queue.pop(0)
                cur_level.append(tmp.val)
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
            res.append(cur_level[::flag])
            flag *= -1
        return res


if __name__ == '__main__':
    a = TreeNode(3)
    b = TreeNode(5)
    c = TreeNode(6)
    d = TreeNode(2)
    e = TreeNode(7)
    f = TreeNode(4)
    g = TreeNode(1)
    h = TreeNode(0)
    i = TreeNode(8)
    # j = TreeNode(1)
    a.right = g
    a.left = b
    b.right = d
    b.left = c

    print(Solution().levelOrder1(a))
    print(Solution().levelOrder2(a))
    print(Solution().levelOrder3(a))


    """        
        # queue = []
        # rs = []
        # if root:
        #     queue.append(root)
        #     while queue:
        #         cur_level,size = [],len(queue)
        #         for _ in range(size):
        #             tmp = queue.pop(0)
        #             cur_level.append(tmp.val)
        #             if tmp.left:
        #                 queue.append(tmp.left)
        #             if tmp.right:
        #                 queue.append(tmp.right)
        #         rs.append(cur_level[:])
        # return rs

    """