"""
easy 2021-12-02 二叉树属性
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node'):# -> int:
        if not root:return 0
        depth = 0
        for x in root.children:
            depth = max(depth, self.maxDepth(x))
        return depth+1

if __name__ == '__main__':
    pass