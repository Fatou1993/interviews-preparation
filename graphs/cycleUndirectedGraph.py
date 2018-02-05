'''Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.'''


# Your task is to complete this function
# Function should return True/False or 1/0
# Graph(graph) is a defaultict of type List
# n is no of Vertices's
def find_parent(u, parent):
    # path compression
    if parent[u] != u:
        parent[u] = find_parent(parent[u], parent)
    return parent[u]


def union(u_p, v_p, parent, rank):
    # union by rank
    if rank[u_p] > rank[v_p]:
        parent[v_p] = u_p
    else:
        parent[u_p] = v_p
        if rank[v_p] == rank[u_p]:
            rank[v_p] += 1


def isCyclic(n, graph):
    # Code here
    parent = [u for u in range(n)]
    rank = [0] * (n)
    edges = [[(u, v) for v in graph[u]] for u in range(n) if u in graph]
    edges.sort()
    edges = list(set(edges))
    print(edges)
    for u in graph:
        for v in graph[u]:
            u_p = find_parent(u, parent)
            v_p = find_parent(v, parent)
            if u_p == v_p:
                return True
            union(u_p, v_p, parent, rank)
    return False

