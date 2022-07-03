"""
middle 2021-12-27 层次遍历ac
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node'):# -> List[List[int]]:
        if not root:return []
        q, res = [root], []
        while q:
            cur_level, size = [],len(q)
            for i in range(size):
                node = q.pop(0)
                cur_level.append(node.val)
                # for j in node.children: # 是这里错啦，遍历每个孩子
                #     q.append(j)
                if node.children:
                    q.extend(node.children) # 使用extend快一点
            res.append(cur_level[:])
        return res

if __name__ == '__main__':
    pass