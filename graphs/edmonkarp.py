from collections import defaultdict, deque
from sets import Set

def initialize_residual_graph(graph):
    """
    Creates edge (v,u) if not already present and add a capacity 0 to it
    :param graph: dictionary of dict : graph[u][v] = capacity edge (u,v) ex.
    :return:
    """
    rgraph = dict(graph)
    for u in graph:
        for v in graph[u] :
            if not v in rgraph:
                rgraph[v] = {u:0}
            elif not u in rgraph[v]:
                rgraph[v][u] = 0
    return rgraph

def updateCapacities(graph, path, max_capacity):
    """
    Update capacities
    :param graph:
    :param path:
    :return:
    """
    n = len(path)
    for i in range(n-1):
        u, v = path[i], path[i+1]
        graph[u][v] -= max_capacity[0]
        graph[v][u] += max_capacity[0]


def isExistAnAugmentingPath(graph, source, sink, parent):
    q = deque([source])
    visited = Set([source])
    while q :
        u = q.popleft()
        if u == sink :
            return True
        for v in graph[u]:
            if graph[u][v] > 0 and not v in visited: #possible to use that edge and vertice not seen before
                parent[v] = u
                visited.add(v)
                q.append(v)
    return False


def getPath(graph, parent, u, source, max_capacity):
    """
    Get a shortest path from source to sink obtained through bfs
    :param graph:
    :param parent: parent[u] stores the parent of u in bfs search
    :param u:
    :param source:
    :param max_capacity: max flow possible on that path
    :return:
    """
    if u == source :
        path = [u]
    else :
        v = parent[u]
        max_capacity[0] = min(max_capacity[0], graph[v][u])
        path = getPath(graph, parent, v, source, max_capacity)
        path.append(u)
    return path


def findMaxFlow(graph, source, sink):
    """
    Find max flow from a graph that can go from source to sink
    :param graph: dictionary of dict : graph[u][v] = capacity edge (u,v)
    :param N: number of vertices
    :return:
    """
    graph = initialize_residual_graph(graph)
    print(graph)
    parent = {}
    max_flow = 0
    while isExistAnAugmentingPath(graph, source, sink, parent):
        max_capacity = [float("inf")]
        path = getPath(graph, parent, sink, source, max_capacity)
        max_flow += max_capacity[0]
        updateCapacities(graph, path, max_capacity)
        parent = {}
    return max_flow

if __name__ == "__main__":
    N, M = 5, 4
    vals = map(int, "1 2 1 3 2 2 4 2 3 2 5 5".strip().split(" "))
    graph = defaultdict(dict)
    for i in range(0, 3 * M - 2, 3):
        u, v, c = vals[i], vals[i + 1], vals[i + 2] #u v,u already there
        graph[u][v] = c
    max_flow = findMaxFlow(graph, 1, N)
    print(max_flow)






