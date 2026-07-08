# bai15.py
import sys

def dijkstra_basic(graph, start, n):
    dist = [sys.maxsize] * n
    dist[start] = 0
    visited = [False] * n

    for _ in range(n):
        # Tim dinh chua tham co khoang cach nho nhat
        u = -1
        min_dist = sys.maxsize
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i
        
        if u == -1:
            break
            
        visited[u] = True

        # Cap nhat khoang cach cac dinh ke
        for v, weight in graph[u]:
            if not visited[v] and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

    return dist

if __name__ == "__main__":
    n = 5 # So dinh tu 0 den 4
    # Do thi dang danh sach ke: graph[u] = [(v, weight), ...]
    graph = {i: [] for i in range(n)}
    graph[0].append((1, 10))
    graph[0].append((4, 5))
    graph[1].append((2, 1))
    graph[1].append((4, 2))
    graph[2].append((3, 4))
    graph[3].append((0, 7))
    graph[3].append((2, 6))
    graph[4].append((1, 3))
    graph[4].append((2, 9))
    graph[4].append((3, 2))

    start_node = 0
    distances = dijkstra_basic(graph, start_node, n)
    
    print(f"Khoang cach tu dinh {start_node}:")
    for i in range(n):
        print(f"Den dinh {i}: {distances[i]}")