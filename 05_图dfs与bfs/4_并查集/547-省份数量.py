"""
middle 2021-12-15 并查集
【并查集的典型应用是有关连通分量的问题】
题目：考察连通分量的数目，在模板中额外添加一个变量去跟踪集合的数量（有多少棵树）。
# 1、初始化的时候把集合数量+1
# 2、合并的时候让集合数量-1
https://leetcode-cn.com/problems/number-of-provinces/solution/python-duo-tu-xiang-jie-bing-cha-ji-by-m-vjdr/
"""

# 怎么把问题转为求并查集呢？思考who和who有关系
# 什么当作节点呢? 城市当作节点

# 1、默写并查集模板
class unionFind:
    def __init__(self):
        self.father = {}
        # 额外记录集合的数量
        self.num_of_sets = 0

    def find_father(self, x):

        root = x
        while self.father[root] is not None:
            root = self.father[root]

        # 在找到x节点的root之后，对剩余节点进行路径压缩，采用迭代方式
        while x != root:
            ori_father = self.father[x]
            self.father[x] = root  # 固定树高度为2
            x = ori_father

        return root

    def union(self, x, y):
        x_father, y_father = self.find_father(x), self.find_father(y)
        if x_father != y_father: # 注意这里，第一次没写
            self.father[x_father] = y_father  # x的父亲是y
            self.num_of_sets -= 1 # 合并的时候让集合数量-1

    # def is_connected(self, x, y):
    #     return self.find_father(x) == self.find_father(y)

    def add(self, x):
        self.father[x] = None
        self.num_of_sets += 1 # 初始化的时候把集合数量+1


class Solution:
    def findCircleNum(self, isConnected): #List[List[int]]) -> int:
        n = len(isConnected)
        #  isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连
        uf = unionFind()
        for i in range(n):
            # add?
            uf.add(i) # 总共3个城市，将每个城市加入到并查集中，count++
            # print('i', i)
            for j in range(i): # 是个对角线啊，i和j连，必然j和i连
                # merge?
                # print(i,j, isConnected[i][j]) # 如果城市i和城市j相连，添加一条边，将i，j放到一个set中
                if isConnected[i][j]:
                    uf.union(i,j)

        return uf.num_of_sets



if __name__ == '__main__':
    # isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    isConnected = [[1,1,1],[1,1,1],[1,1,1]] # 1
    print(Solution().findCircleNum(isConnected))