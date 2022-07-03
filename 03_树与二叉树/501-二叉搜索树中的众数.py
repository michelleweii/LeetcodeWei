"""
easy 2021-12-29 BST中序遍历是升序的
https://www.programmercarl.com/0501.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E4%BC%97%E6%95%B0.html#%E9%80%92%E5%BD%92%E6%B3%95
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.pre = None  # 记录前一个节点
        self.maxcount = -1 # 最大频率
        self.count = -1 # 统计频率
        self.res = []

    def findMode(self, root: TreeNode):# -> List[int]:
        self.search_bst(root)
        return self.res

    def search_bst(self, cur):
        if not cur:return

        self.search_bst(cur.left)

        # 根处理操作
        if self.pre is None: self.count = 1 # 第一个节点(第一次出现，那么数量是1)
        elif self.pre.val == cur.val: self.count += 1 # 与前一个节点数值相同（第n次出现，数量++）
        else: self.count = 1 #与前一个节点数值不同

        self.pre = cur # 更新上一个节点

        if self.count==self.maxcount: #  如果和最大值相同，放进result中
            self.res.append(cur.val)

        if self.count>self.maxcount: # 如果计数大于最大值频率
            self.res = [] # 很关键的一步，不要忘记清空result，之前result里的元素都失效了
            self.maxcount = self.count # 更新最大频率
            self.res.append(cur.val)

        self.search_bst(cur.right)
        # return

if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(2)
    a.right = b
    b.left = c
    print(Solution().findMode(a))