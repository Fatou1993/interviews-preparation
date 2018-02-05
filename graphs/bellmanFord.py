def relax(vertices, u, v, w):
    if vertices[v].dist > vertices[u].dist + w :
        vertices[v].dist = vertices[u].dist + w

def hasNegativeCycle(edges, vertices, N):
    """
    Idea :
    use
    :param graph:
    :return:
    """
    for _ in range(N-1):
        for edge in edges :
            u, v, w = edge
            relax(vertices, u, v, w)

    for edge in edges:
        u, v, w = edge
        if vertices[v].dist > vertices[u].dist + w:
            return True
    return False

