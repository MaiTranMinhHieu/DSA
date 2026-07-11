import heapq
g1 = {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5), (4, 8)], 3: [(4, 3), (5, 6)], 4: [(5, 2)], 5: []}
def dijkstra(g, start):
    dist = {n: float('inf') for n in g}; dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        for v, w in g[u]:
            if d + w < dist[v]:
                dist[v] = d + w; heapq.heappush(pq, (dist[v], v))
    return dist
print("Khoảng cách tới mọi đỉnh:", dijkstra(g1, 0))