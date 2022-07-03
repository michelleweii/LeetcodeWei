"""
easy 2021-12-26 递归遍历
类似LC101 LC572
思路一：前序遍历两棵树，结果一样则相同;
思路二：递归遍历检查每个节点是否相同
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p == null && q == null) 
            return true;
        if(p == null || q == null) 
            return false;
        if(p.val != q.val) 
            return false;
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}
"""
class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q: return True  # [],[]
        if not p or not q: return False  # [],[1,2]
        if p.val != q.val: return False
        return self.check(p, q)

    def check(self, root1, root2):
        if not root1 and not root2: return True
        if not root1 or not root2: return False
        if root1.val != root2.val: return False
        return self.check(root1.left, root2.left) and self.check(root1.right, root2.right)

    def isSameTree_old(self, p, q):
        res1,res2 = [],[]
        if self.preorder(p,res1)==self.preorder(q,res2):
            return True
        return False

    def preorder(self,root,res):
        if root:
            res.append(root.val)
            if root.left:
                self.preorder(root.left,res)
            else:
                res.append('null')
            if root.right:
                self.preorder(root.right,res)
            else:
                res.append('null')
        return res

if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(1)
    d = TreeNode(2)
    a.left = b
    c.right = d
    print(Solution().isSameTree(a,c))