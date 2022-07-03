if __name__ == '__main__':
    # # line1 = list(map(int, input().split()))
    # # num_node = line1[0]
    # # num_vertice = line1[1]
    # num_node = 4
    # num_vertice = 6
    # no_direct_graph = [[0, 1, 4],[0, 2, 3],[0, 3, 1],[1, 2, 1],[1, 3, 2],[2, 3, 5]]
    #
    # # for i in range(num_vertice):
    # #     no_direct_graph.append(list(map(int, input().split())))
    #
    # start_end = [0,1]
    #     #list(map(int, input().split()))

    line1 = list(map(int, input().split()))
    num_node = line1[0]
    num_vertice = line1[1]

    no_direct_graph = []

    for i in range(num_vertice):
        no_direct_graph.append(list(map(int, input().split())))

    start_end = [0]

    dict_graph = {}
    for k in range(len(no_direct_graph)):  # 对于无向图中的每一条边
        for j in range(num_node):
            if no_direct_graph[k][0] == j + 1:
                if j + 1 not in dict_graph:
                    dict_graph[j + 1] = [no_direct_graph[k]]
                else:
                    dict_graph[j + 1].append(no_direct_graph[k])
            elif no_direct_graph[k][1] == j + 1:
                if j + 1 not in dict_graph:
                    dict_graph[j + 1] = [
                        [no_direct_graph[k][1], no_direct_graph[k][0], no_direct_graph[k][2]]]
                else:
                    dict_graph[j + 1].append(
                        [no_direct_graph[k][1], no_direct_graph[k][0], no_direct_graph[k][2]])
    # print(dict_graph)  # 以字典的形式构造无向图

    visited = []
    unvisited = [_ + 1 for _ in range(num_node)]

    distance = [float('inf') for _ in range(num_node)]

    money = [0 for _ in range(num_node)]

    temp = start_end[0]
    # money[temp - 1] = 0
    distance[temp] = 0
    for j in range(num_node):
        temp_neighbor = dict_graph[temp]
        for route in temp_neighbor:
            print('route',route)
            if route[1] not in visited:  # 如果当前节点的邻居节点没有被访问过
                if distance[temp] + route[2] < distance[route[1]]:
                    distance[route[1] ] = distance[temp] + route[2]
                    # print(route[-1])
                    money[route[1]] = money[temp ] + route[-1]
        distance_compare = distance.copy()
        distance_compare[temp] = float("inf")

        visited.append(temp)
        if temp in unvisited:
            unvisited.remove(temp)

        min_value = float("inf")
        min_index = 0

        for k in range(num_node):
            if k + 1 in unvisited:  # 如果当前的节点并没有被访问过
                if distance_compare[k] < min_value:
                    min_value = distance_compare[k]
                    min_index = k
        temp = min_index + 1

    print(min(distance))
