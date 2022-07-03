"""
middle 2021-12-09 bfs遍历
这道题就是遍历整个图（bfs or dfs），所以遍历时候要记录已经访问点，用{}记录。map:{old,new} # {原图node,新图node}
https://leetcode-cn.com/problems/clone-graph/solution/ke-long-tu-by-leetcode-solution/
时间复杂度O(V+E)
1、遍历原图的每个点，建立新的点；
2、点建立完成后，再建立新的边（注意新的边是建立在新点中）；
"""
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution:
    # bfs 遍历图
    # """
    # # 1、使用一个哈希表 visited 存储所有已被访问和克隆的节点。哈希表中的 key 是原始图中的节点，value 是克隆图中的对应节点。
    # # 2、将题目给定的节点添加到队列。克隆该节点并存储到哈希表中。
    # # 3、每次从队列首部取出一个节点，遍历该节点的所有邻接点。如果某个邻接点已被访问，则该邻接点一定在 visited 中，那么从 visited 获得该邻接点，
    # # 否则创建一个新的节点存储在 visited 中，并将邻接点添加到队列。将克隆的邻接点添加到克隆图对应节点的邻接表中。重复上述操作直到队列为空，则整个图遍历结束。
    # """
    def cloneGraph(self, node):
        if not node: return node
        # queue存放原图node
        queue = []
        queue.append(node)
        # 克隆第一个节点并存储到哈希表中
        visited = {} # map:{old,new} # {原图node,新图node}
        visited[node] = Node(node.val, [])
        # 广度优先搜索
        while queue:
            # 取出队列的头节点, 例如node1
            n = queue.pop(0)
            # 遍历该节点的邻居
            for neighbor in n.neighbors: # 例如node1的2,4
                # 1、创建点
                if neighbor not in visited:
                    # 如果没有被访问过，就克隆并存储在哈希表中
                    # 原图node：neighbor.val
                    # 新图node：Node(neighbor.val, [])
                    # 建立映射关系 {2:2`}
                    visited[neighbor] = Node(neighbor.val, [])
                    # 将邻居节点加入队列中
                    queue.append(neighbor) # queue=[2]

                # 2、创建边(建点之后就建边)
                # 更新当前节点的邻居列表，新点——新边
                # 【注意】
                # visited[n] 新点，是个Node数据结构
                # n 旧点
                visited[n].neighbors.append(visited[neighbor])
        #
        # print(visited[node].val) # 1
        return visited[node] # 返回新图起始点

# dfs遍历图
# """

# """
class Solution(object):
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node):
        if not node:
            return node
        # 如果该节点已经被访问过了，则直接从哈希表中取出对应的克隆节点返回
        if node in self.visited:
            return self.visited[node]
        # 克隆节点，注意到为了深拷贝我们不会克隆它的邻居的列表
        clone_node = Node(node.val, [])
        # 哈希表存储
        self.visited[node] = clone_node
        # 遍历该节点的邻居并更新克隆节点的邻居列表
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node



if __name__ == '__main__':
    """
    输入：adjList = [[2,4],[1,3],[2,4],[1,3]]
    输出：[[2,4],[1,3],[2,4],[1,3]]
    解释：
        图中有 4 个节点。
        节点 1 的值是 1，它有两个邻居：节点 2 和 4 。
        节点 2 的值是 2，它有两个邻居：节点 1 和 3 。
        节点 3 的值是 3，它有两个邻居：节点 2 和 4 。
        节点 4 的值是 4，它有两个邻居：节点 1 和 3 。
    """
    # adjList = [[2,4],[1,3],[2,4],[1,3]]
    # print(Solution().cloneGraph(adjList))
    pass