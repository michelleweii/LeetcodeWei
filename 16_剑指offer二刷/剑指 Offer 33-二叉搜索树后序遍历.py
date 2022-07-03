"""
middle BST
2021-07-16
bst 二叉搜索树的中序遍历是递增的
需要重做https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/solution/mian-shi-ti-33-er-cha-sou-suo-shu-de-hou-xu-bian-6/
"""
class Solution:
    # RecursionError: maximum recursion depth exceeded.
    # python的递归深度是有限制的，默认为1000
    def verifyPostorder1(self, postorder):
        self.postorder = postorder
        return self.dfs(0, len(postorder) - 1)

    def dfs(self, l, r):
        # 定义dfs的出口
        if l >= r: return True
        root = self.postorder[r]
        k = l
        while k < r and self.postorder[k] < root: k += 1
        mid = k
        while self.postorder[k] > root: k += 1
        return k == r and self.dfs(l, mid - 1) and self.dfs(mid, r - 1)

    def dfs2(self, l, r):
        # 定义dfs的出口
        if l>=r:return True
        root = self.postorder[r]
        k = l
        while k<r and self.postorder[k]<root:k+=1
        for i in range(k, r):
            if self.postorder[i]<root: return False
        return self.dfs(l, k-1) and self.dfs(k, r-1)

    def verifyPostorder(self, postorder):
        def dfs(l, r):
            if l >= r: return True
            k = l
            while postorder[k] < postorder[r]: k += 1
            m = k
            while postorder[k] > postorder[r]: k += 1
            return k == r and dfs(l, m - 1) and dfs(m, r - 1)

        return dfs(0, len(postorder) - 1)

if __name__ == '__main__':
    postorder = [1,3,2,6,5]
    print(Solution().verifyPostorder(postorder))