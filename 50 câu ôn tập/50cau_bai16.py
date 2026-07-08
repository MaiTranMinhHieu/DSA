# bai16.py
import sys

def dijkstra_path(graph, start, target, n):
    dist = [sys.maxsize] * n
    parent = [-1] * n
    dist[start] = 0
    visited = [False] * n

    for _ in range(n):
        u = -1
        min_dist = sys.maxsize
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i
        
        if u == -1: break
        visited[u] = True

        for v, weight in graph[u]:
            if not visited[v] and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                parent[v] = u  # Luu vet

    # Truy vet
    path = []
    curr = target
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    path.reverse()
    
    return dist[target], path

if __name__ == "__main__":
    n = 5
    graph = {i: [] for i in range(n)}
    graph[0].extend([(1, 10), (4, 5)])
    graph[1].extend([(2, 1), (4, 2)])
    graph[2].append((3, 4))
    graph[4].extend([(1, 3), (2, 9), (3, 2)])
    
    s, t = 0, 3
    distance, path = dijkstra_path(graph, s, t, n)
    print(f"Khoang cach ngan nhat tu {s} toi {t}: {distance}")
    print(f"Duong di: {' -> '.join(map(str, path))}")