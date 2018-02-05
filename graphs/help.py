def dfs(u, adj, visited, disc, low, stack, time, parent, odd, even):
    visited[u]=True
    time[0]+=1
    disc[u] = low[u] = time[0]
    child = 0
    for v in adj[u]:
        if parent[u] == v :
            continue
        if not visited[v]:
            parent[v] = u
            child += 1
            stack.append((u,v))
            dfs(v, adj, visited, disc, low, stack, time, parent, odd, even)
            low[u] = min(low[u], low[v])
            if (parent[u] != -1 and disc[u] <= low[v]) or (parent[u] == -1 and child >= 2): #articulation point
                numEdgesInComponent = 0
                while stack[-1] != (u,v):
                    stack.pop()
                    numEdgesInComponent += 1
                stack.pop() #pop (u,v)
                numEdgesInComponent += 1
                if numEdgesInComponent %2 :
                    odd[0]+=1
                else:
                    even[0]+=1
        elif disc[v] < low[u]:
            low[u] = disc[v] #back edges
            stack.append((u,v))