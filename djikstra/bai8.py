import heapq
g1 = {0: [(1,4), (2,1)], 1: [(3,1)], 2: [(1,2), (3,5), (4,8)], 3: [(4,3), (5,6)], 4: [(5,2)], 5: []}
def bai_8(g, s, D):
    dist = {n: float('inf') for n in g}; dist[s] = 0
    pq = [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        for v, w in g[u]:
            if d + w < dist[v]: dist[v] = d + w; heapq.heappush(pq, (dist[v], v))
    print(f"Các đỉnh trong bán kính {D}:", [n for n, d in dist.items() if d <= D])
bai_8(g1, 0, 3)