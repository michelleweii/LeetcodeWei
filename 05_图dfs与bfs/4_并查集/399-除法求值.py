"""
middle 2021-12-15 带权并查集、Floyd算法
核心思想：被除数当作子节点，除数当作父节点
并查集：https://leetcode-cn.com/problems/evaluate-division/solution/pythonbing-cha-ji-fu-mo-ban-by-milomusia-kfsu/
基础题：lc547（不带权并查集）

# who和who有关系？ 除数与被除数有关系，两者有个边
"""
# Floyd:https://leetcode-cn.com/problems/evaluate-division/solution/tu-lun-wen-ti-floydsuan-fa-by-jun-heng-jpxo/
# 首先默写并查集
class unionFind:
    def __init__(self):
        """
        记录每个节点的父节点
        记录每个节点到根节点的权重
        """
        self.father = {} # 记录每个节点的父节点
        self.value = {} # # 【带权新增】记录每个节点到根节点的权重

    def find_father(self, x):
        """
        1\查找根节点
        2\路径压缩
        3\更新权重
        """
        root = x
        # # 【带权新增】节点更新权重的时候要放大的倍数
        base = 1  # 对于最下边的节点，初始化倍数为1，我们要计算最下面的节点除以根节点的值，用于后续压缩快速计算压缩节点的权值，方法和merge一样
        # 迭代找到x的父节点，从而找到根节点
        while self.father[root] != None:
            root = self.father[root]
            base *= self.value[root] #【带权新增】

        # 找到根节点的开始路径压缩
        while x!=root:
            ori_father = self.father[x] # 保存上一个父亲节点
            ##### 离根节点越远，放大的倍数越高
            self.value[x] *= base  # 前面讲了，base是最下面的节点除以根节点的值，此时x直接链接根，乘回去即可
            base /= self.value[ori_father] # 少了最小面的节点，缩小base
            #####
            self.father[x] = root # 改变当前节点父亲节点，就需要改变其权值，从最小开始，前面缓存了最下面的base
            x = ori_father
        return root

    def union(self, x, y, val):
        # 找x的根节点，y的根节点，两者相连
        x_father, y_father = self.find_father(x), self.find_father(y) # 此时x val代表x除以root_x的值，y val代表y除以root_y的值
        if x_father != y_father:
            self.father[x_father] = y_father # 画图可知，root_x多了father为root_y，需要修改其权重
            ##### 四边形法则更新根节点的权重
            self.value[x_father] = self.value[y] * val / self.value[x] # 四边形法则是啥？


    def is_connected(self, x, y):
        # x,y的根节点是否相同
        # 【带权新增】x in self.value and y in self.value
        # 前后顺序不能交换
        return x in self.value and y in self.value and self.find_father(x)==self.find_father(y)

    def add(self, x):
        if x not in self.father: # 关键竟然在这里！
            self.father[x] = None # 新节点初始化，必然是没有父节点的
            self.value[x] = 1.0 # 【带权新增】添加新节点，初始化权重为1.0


class Solution:
    def calcEquation(self, equations, values, queries):
        uf = unionFind()
        # 创建并查集
        for (a,b), val in zip(equations, values):
            # print((a,b), val)
            uf.add(a)
            uf.add(b)
            uf.union(a,b,val)

        res = [-1.0] * len(queries)

        for i, (a, b) in enumerate(queries):
            # print(i, (a, b))
            if uf.is_connected(a, b):
                res[i] = uf.value[a] / uf.value[b]

        return res

if __name__ == '__main__':
    # equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
    # values = [1.5, 2.5, 5.0]
    # queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
    # # [3.75000,0.40000,5.00000,0.20000]

    # equations = [["a", "b"], ["b", "c"]]
    # values = [2.0, 3.0]
    # queries = [["a", "c"], ["b", "a"], ["a", "e"],["a", "a"], ["x", "x"]]

    equations = [["a", "b"], ["e", "f"], ["b", "e"]]
    values = [3.4, 1.4, 2.3]
    queries = [["b", "a"], ["a", "f"], ["f", "f"], ["e", "e"], ["c", "c"], ["a", "c"], ["f", "e"]]
    # [0.29412,10.948,1.0,1.0,-1.0,-1.0,0.71429]
    print(Solution().calcEquation(equations,values,queries))