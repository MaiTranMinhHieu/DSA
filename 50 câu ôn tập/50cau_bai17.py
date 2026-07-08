# bai17.py
import heapq
import sys

def dijkstra_heap(graph, start, n):
    dist = [sys.maxsize] * n
    dist[start] = 0
    pq = [(0, start)] # (distance, node)
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]:
            continue
            
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
                
    return dist

if __name__ == "__main__":
    n = 5
    graph = {i: [] for i in range(n)}
    graph[0].extend([(1, 10), (4, 5)])
    graph[1].extend([(2, 1), (4, 2)])
    graph[2].append((3, 4))
    graph[3].extend([(0, 7), (2, 6)])
    graph[4].extend([(1, 3), (2, 9), (3, 2)])

    distances = dijkstra_heap(graph, 0, n)
    print("Khoang cach voi Dijkstra Min-Heap:", distances)