from collections import deque

def shortest_path(V, edges, start, end):
    graph = [[] for _ in range(V)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * V
    dist = [-1] * V
    queue = deque([start])
    
    visited[start] = True
    dist[start] = 0
    
    while queue:
        node = queue.popleft()
        
        if node == end:
            return dist[node]
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    
    return -1
# V = 5
# edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]]
# start = 0
# end = 4
# V = 3
# edges = [[0, 1], [1, 2]]
# start = 0
# end = 2
V = 4
edges = [[0, 1], [1, 2]]
start = 2
end = 3

print(shortest_path(V, edges, start, end))
