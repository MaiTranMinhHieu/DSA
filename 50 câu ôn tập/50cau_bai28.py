from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    res = []
    while queue:
        node = queue.popleft()
        res.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return res

graph_bfs = {1: [2, 3], 2: [4, 5], 3: [6], 4: [], 5: [], 6: []}
print(bfs(graph_bfs, 1))