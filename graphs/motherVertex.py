from collections import defaultdict

class Graph :
    def __init__(self, V):
        self.V = V
        self.graph = {}

    def addEdge(self, u, v):
        if not u in self.graph :
            self.graph[u] = []
        self.graph[u].append(v)

def simpledfs(u, graph, visited):
    visited.add(u)
    if u in graph :
        for v in graph[u]:
            if not v in visited :
               simpledfs(v, graph, visited)


def dfs(u, graph, visited, time, finishTime):
    visited.add(u)
    time[0]+=1
    if u in graph :
        for v in graph[u]:
            if not v in visited :
                dfs(v, graph, visited, time, finishTime)
    time[0]+=1
    finishTime[u] = time[0]

def motherVertex(graph, N):
    time = [0]
    finishTime = [0]*N
    visited = set()
    for u in range(N) :
        if not u in visited :
            dfs(u, graph, visited, time, finishTime)
    lastFinishVertex = [u for u in range(N) if finishTime[u] == time[0]][0]
    visited = set()
    time[0] = 0
    simpledfs(lastFinishVertex, graph, visited)
    if len(visited) == N : #all elements have been visited :
        return lastFinishVertex
    else:
        return None

if __name__ == "__main__":
    N = 7
    g = {}
    g[0] = [1, 2]
    g[1] = [3]
    g[4] = [1]
    g[6] = [4, 0]
    g[5] = [6, 2]
    print(motherVertex(g, 7))




