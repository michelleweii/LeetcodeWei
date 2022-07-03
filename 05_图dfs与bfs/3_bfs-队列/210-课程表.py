"""
middle 2021-12-09 拓扑排序
拓扑排序，基础题207，207返回是否合理
本题需要打印图的路径
这个问题相当于查找一个循环是否存在于有向图中。如果存在循环，则不存在拓扑排序，因此不可能选取所有课程进行学习。

# 【Note】
1、邻接表：通过结点的索引，我们能够得到这个结点的后继结点；
2、入度数组：通过结点的索引，我们能够得到指向这个结点的结点个数。
# 拓扑排序检查有向图是否有环
# 并查集检查无向图是否有环
"""
class Solution:
    def findOrder(self, numCourses, prerequisites):
        # 入度表，建图（邻接矩阵）
        indegrees = [0 for _ in range(numCourses)]
        graph = [[] for _ in range(numCourses)]

        # 初始化入度表+邻接矩阵
        for item in prerequisites:
            after = item[0]
            before = item[1]
            indegrees[after] += 1 # 入度+1
            graph[before].append(after) # 相邻节点++

        # print('indegrees', indegrees)

        queue = []
        # 找到所有入度为0的点
        for i in range(numCourses): # 遍历每一门课程
            if indegrees[i]==0:
                queue.append(i)

        res = [] # 保存课程路径
        # BFS
        while queue:
            cur_course = queue.pop(0)
            # 修完一门课程
            res.append(cur_course)
            numCourses -= 1
            # 去修该门课程的剩余课程，遍历邻接矩阵
            for next_course in graph[cur_course]:
                # 将next_course的入度都-1，因为cur_course已经消灭了
                indegrees[next_course] -= 1
                # 如果-1之后入度为0，说明依赖都解决了，可以开始了
                if indegrees[next_course] == 0:
                    queue.append(next_course)
        if numCourses==0:
            return res
        else:return []

if __name__ == '__main__':
    # numCourses = 2
    # prerequisites = [[1, 0]]
    numCourses = 3
    prerequisites = [[1, 0], [1, 2], [0, 1]]
    print(Solution().findOrder(numCourses, prerequisites))