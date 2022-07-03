# -*- coding:utf-8 -*-
# 需要重做
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        if self.isPart(pRoot1,pRoot2): return True
        return self.HasSubtree(pRoot1.left,pRoot2) \
               or self.HasSubtree(pRoot1.right,pRoot2)
    def isPart(self,p1,p2):
        # 如果p2是空，说明小的子树遍历结束
        if not p2: return True
        if not p1 or (p1.val != p2.val): return False
        return self.isPart(p1.left,p2.left) \
               and self.isPart(p1.right,p2.right)


