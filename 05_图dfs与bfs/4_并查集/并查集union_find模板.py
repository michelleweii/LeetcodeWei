# https://leetcode-cn.com/problems/number-of-provinces/solution/python-duo-tu-xiang-jie-bing-cha-ji-by-m-vjdr/

class UnionFind:
    def __init__(self):
        """
        记录每个节点的父节点
        """
        self.father = {}

    def find(self, x):
        """
        查找根节点+路径压缩
        """
        root = x

        while self.father[root] != None:
            root = self.father[root] # 找到根节点

        # 路径压缩
        # 核心思想：树的高度固定为2
        # 实现方式：迭代
        while x != root:
            original_father = self.father[x] # x节点原始的father
            self.father[x] = root # 将x节点的father重设为root根节点，实现固定长度为2
            x = original_father # 再来新的一轮重置

        return root

    def merge(self, x, y, val):
        """
        合并两个节点
        """
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            self.father[root_x] = root_y # y的父节点是x，交换一下也没有关系

    def is_connected(self, x, y):
        """
        判断两节点是否相连
        """
        return self.find(x) == self.find(y) # 父节点相等则连接

    def add(self, x):
        """
        添加新节点
        """
        if x not in self.father:
            self.father[x] = None

# 模板题
# 399. 除法求值 https://leetcode-cn.com/problems/evaluate-division/
# 721. 账户合并 https://leetcode-cn.com/problems/accounts-merge/
# 803. 打砖块 https://leetcode-cn.com/problems/bricks-falling-when-hit/
# 1632. 矩阵转换后的秩 https://leetcode-cn.com/problems/rank-transform-of-a-matrix/