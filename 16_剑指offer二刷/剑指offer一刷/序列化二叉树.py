# -*- coding:utf-8 -*-
# 请实现两个函数，分别用来序列化和反序列化二叉树
# https://blog.csdn.net/fuxuemingzhu/article/details/79725343
# https://blog.csdn.net/u010005281/article/details/79787278
class TreeNode:
    """
     1. 对于序列化：使用前序遍历，递归的将二叉树的值转化为字符，并且在每次二叉树的结点
        不为空时，在转化val所得的字符之后添加一个' ， '作为分割。对于空节点则以 '#' 代替。
     2. 对于反序列化：按照前序顺序，递归的使用字符串中的字符创建一个二叉树(特别注意：
    在递归时，递归函数的参数一定要是char ** ，这样才能保证每次递归后指向字符串的指针会
    随着递归的进行而移动！！！)
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Serialize(self, root):
        self.res = ""
        self.helper(root)
        return self.res
    def helper(self,root):
        if not root:
            self.res += "#,"
            return
        #     s = '$,' 等价
        #     return s
        self.res += str(root.val)+','
        self.helper(root.left)
        self.helper(root.right)

    def Deserialize(self, s):
        lista = s.split(',')
        return self.helper_de(lista)

    def helper_de(self,tree):
        if not tree:return None
        val = tree.pop(0)
        root = None
        if val != "#":
            root = TreeNode(int(val))
            root.left = self.helper_de(tree)
            root.right = self.helper_de(tree)
        return root


if __name__ == '__main__':
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    d = TreeNode(15)
    e = TreeNode(7)
    a.right = c
    a.left = b
    c.right = e
    c.left = d
    res = Solution().Serialize(a)
    #[3,9,20,#,#,15,7]
    print(Solution.Deserialize(res))
