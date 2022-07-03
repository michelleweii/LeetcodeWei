"""
middle 2021-11-14 树回溯
https://programmercarl.com/0112.%E8%B7%AF%E5%BE%84%E6%80%BB%E5%92%8C.html#%E8%BF%AD%E4%BB%A3
找到所有路径，所以递归函数不要返回值！
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.path, self.res = [], []
    def pathSum(self, root, targetSum):
        if not root:return self.res
        self.path.append(root.val)
        self.dfs(root, targetSum-root.val)
        return self.res
    # 递归函数不需要返回值，因为我们要遍历整个树
    def dfs(self, root, target):
        # 遇到了叶子节点且找到了和为sum的路径
        if target==0 and not root.right and not root.left:
            self.res.append(self.path[:])
            return
        # 遇到叶子节点而没有找到合适的边，直接返回
        if not root.right and not root.left:
             return

        if root.left:
            target -= root.left.val
            self.path.append(root.left.val)
            self.dfs(root.left, target) # 递归
            target += root.left.val # 回溯
            self.path.pop() # 回溯

        if root.right:
            target -= root.right.val
            self.path.append(root.right.val)
            self.dfs(root.right, target) # 递归
            target += root.right.val # 回溯
            self.path.pop() # 回溯
        # return
#---------------------------------------- 2021-11-14 -----------------------------------------------------------
    # 1.使用何种数据结构存储遍历路径上的节点？
    # 2.在树的前序遍历时做什么？后序遍历时做什么？
    # 3.如何判断一个节点为叶节点？当遍历到叶节点时应该做什么？
    def pathSum_2019(self, root, sum):
        rs, path = [], []
        path_value = 0
        if root is None: return rs
        # return self.preorder(root,sum,path,path_value,rs) # 是None
        self.preorder(root, sum, path, path_value, rs)
        # 因为Python是引用传值，所以这个时候执行完preorder函数，rs已经改变了
        return rs
    # 深度遍历——前序遍历
    def preorder(self,node,sum,path,path_value,rs):
        if node is None: return
        # 此时访问node为前序遍历
        # 遍历一个节点即更新一次路径值
        path.append(node.val)
        path_value += node.val
        if node.right is None and node.left is None and path_value == sum:
            # rs.append(path.copy())  # path.copy() —— leetcode ide无法通过
            rs.append(path[:])
        self.preorder(node.left, sum, path, path_value, rs)
        self.preorder(node.right, sum, path, path_value, rs)
        # 遍历完成后，叶子节点出栈
        # 这一块的顺序不知道到底放在哪里？
        # 答：左右子树全部访问完，说明以它为根节点的这颗子树已经访问完了，
        # 以它为根节点的所有可能性都尝试了，然后就换一个结点为根节点呀
        del path[-1]
        path_value -= node.val
    #-----------------------------------------------------------------
    def pathSum222(self, root, sum):
        self.res = []
        self.total = sum

        def caculate(root, sum, templist):
            if not root: return
            if not root.left and not root.right:
                if root.val + sum == self.total:
                    self.res.append(templist + [root.val])
            if root.left:
                caculate(root.left, sum + root.val, templist + [root.val])
            if root.right:
                caculate(root.right, sum + root.val, templist + [root.val])

        caculate(root, 0, [])
        return self.res


    #-----------------------------------------------------------------
    def pathSum333(self, root, sum):
        result = list()
        if not root: return result
        self._pathSum(result, list(), root, sum)
        return result

    def _pathSum(self, result, path, node, num):
        if node:
            path.append(node.val)

            if not node.left and not node.right and num == node.val:
                result.append(path.copy())

            self._pathSum(result, path, node.left, num - node.val)
            self._pathSum(result, path, node.right, num - node.val)
            path.pop()


if __name__ == '__main__':
    a = TreeNode(5)
    b = TreeNode(4)
    c = TreeNode(8)
    d = TreeNode(11)
    e = TreeNode(13)
    f = TreeNode(4)
    g = TreeNode(7)
    h = TreeNode(2)
    i = TreeNode(5)
    j = TreeNode(1)
    a.right = c
    a.left = b
    b.left = d
    d.left = g
    d.right = h
    c.right = f
    c.left = e
    f.right = j
    f.left = i
    sum = 22
    # Solution().pathSum(a, sum)
    print(Solution().pathSum(a,sum))



