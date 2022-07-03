"""
middle 2021-12-09 拓扑排序（dfs与bfs都可以实现）
https://leetcode-cn.com/problems/course-schedule/solution/course-schedule-tuo-bu-pai-xu-bfsdfsliang-chong-fa/
题目:课程安排图是否是 有向无环图(DAG)。即课程间规定了前置条件，但不能构成任何环路，否则课程前置条件将不成立。

1、邻接表：通过结点的索引，我们能够得到这个结点的后继结点；
2、入度数组：通过结点的索引，我们能够得到指向这个结点的结点个数。

dfs的实现之后再学习吧：https://leetcode-cn.com/problems/course-schedule/solution/course-schedule-tuo-bu-pai-xu-bfsdfsliang-chong-fa/
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites): #: List[List[int]]) -> bool:
        # 1、邻接表：通过结点的索引，我们能够得到这个结点的后继结点；
        # 2、入度数组：通过结点的索引，我们能够得到指向这个结点的结点个数。
        indegrees = [0 for _ in range(numCourses)] # 入度表
        adjacency = [[] for _ in range(numCourses)] # 邻接表, 用于建图
        # 建表 # Get the indegree and adjacency of every course.
        for cur, pre in prerequisites:
            # print(cur, pre) # 打印当前课程，与当前课程的前驱
            indegrees[cur]+=1 # 当前课程入度+1
            adjacency[pre].append(cur) # 那么前驱节点的邻接矩阵中有‘当前节点’
        # // [1, 2] = 2 -> 1
        # // from = item[1] = 2
        # // to = item[0] = 1
        queue = []
        # 找到起始节点，即入度为0的节点 # Get all the courses with the indegree of 0.
        # 获取所有入度为0的课程
        for i in range(numCourses): # i刚好能和课程对上是题目保证的 `必须选修 numCourses 门课程，记为 0 到 numCourses - 1`
            if indegrees[i]==0: # 如果课程i的入度是0
                queue.append(i)
        # BFS
        while queue:
            pre = queue.pop(0)
            # 学完一个前置课程，课程数-1
            numCourses -= 1
            for next_course in adjacency[pre]:
                indegrees[next_course] -= 1
                if indegrees[next_course] == 0:
                    queue.append(next_course)
        # 若课程安排图中存在环，一定有节点的入度始终不为 0
        # 拓扑排序出队次数等于课程个数，返回 numCourses == 0 判断课程是否可以成功安排
        return numCourses == 0


if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1,0]] # 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
    print(Solution().canFinish(numCourses,prerequisites))