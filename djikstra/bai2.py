import heapq
g1 = {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5), (4, 8)], 3: [(4, 3), (5, 6)], 4: [(5, 2)], 5: []}
def chot_dinh(g, start):
    dist = {n: float('inf') for n in g}; dist[start] = 0
    pq = [(0, start)]; visited = []; chot = []
    while pq:
        d, u = heapq.heappop(pq)
        if u not in chot:
            chot.append(u)
            for v, w in g[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
    return chot
print("Thứ tự chốt đỉnh:", chot_dinh(g1, 0))