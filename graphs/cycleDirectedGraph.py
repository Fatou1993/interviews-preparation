def dfs(u, graph, visited, visiting):
    if visiting[u]:
        return True
    visiting[u] = True
    for v in graph[u]:
        if not visited[v]:
            if dfs(v, graph, visited, visiting):
                return True
    visited[u] = True
    return False


def isCyclic(n, graph):
    # Code here
    visited = [False] * (n)
    visiting = [False] * (n)
    for u in range(n):
        if not visited[u]:
            if dfs(u, graph, visited, visiting):
                return True
    return False
