
def BFS(graph,s): # 开始的节点
    queue = []
    queue.append(s)
    # print(queue)
    seen = set()
    seen.add(s) # hash表，比list要快
    while (len(queue)>0):
        vertex = queue.pop(0)
        # A所有的邻接点
        nodes = graph[vertex]
        # print(nodes)
        # 对于所有没有被访问过的节点，加入队列
        for w in nodes:
            if w not in seen:
                queue.append(w)
                # print(queue)
                seen.add(w)
        print(vertex)

def DFS(graph,s): # 开始的节点
    stack = []
    stack.append(s)
    # print(queue)
    seen = set()
    seen.add(s) # hash表，比list要快
    while (len(stack)>0):
        vertex = stack.pop()
        # A所有的邻接点
        nodes = graph[vertex]
        # print(nodes)
        # 对于所有没有被访问过的节点，加入队列
        for w in nodes:
            if w not in seen:
                stack.append(w)
                # print(queue)
                seen.add(w)
        print(vertex)

# 从A出发到其他所有点的最短距离
def BFSextend(graph,s): # 最短路径
    queue = []
    queue.append(s)
    # print(queue)
    seen = set()
    seen.add(s) # hash表，比list要快
    parent = {s:None}
    while (len(queue)>0):
        vertex = queue.pop(0)
        # A所有的邻接点
        nodes = graph[vertex]
        # print(nodes)
        # 对于所有没有被访问过的节点，加入队列
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
                parent[w] = vertex
        # print(vertex)
    return parent

def main():
    graph = {
        "A": ["B", "C"],
        "B": ["A", "C", "D"],
        "C": ["A", "B", "D", "E"],
        "D": ["B", "C", "E", "F"],
        "E": ["C", "D"],
        "F": ["D"]
    }
    # print(graph.keys())  # dict_keys(['A', 'B', 'C', 'D', 'E', 'F'])
    # print(graph["E"])  # ['C', 'D']
    BFS(graph,"A")
    print('------------')
    DFS(graph, "A")
    print('------------')
    parents = BFSextend(graph,"E")
    for key in parents:
        print(key,parents[key]) # key的前一个点是什么
    print('***************')
    # 从E出发走到B
    end = "B"
    while end != None:
        print(end)
        end = parents[end]

if __name__ == '__main__':
    main()
