import heapq
g1 = {0: [(1,4), (2,1)], 1: [(3,1)], 2: [(1,2), (3,5), (4,8)], 3: [(4,3), (5,6)], 4: [(5,2)], 5: []}
def bai_7(g, s, t):
    dist = {n: float('inf') for n in g}; parent = {n: None for n in g}; dist[s] = 0
    pq = [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        for v, w in g[u]:
            if d + w < dist[v]: dist[v] = d + w; parent[v] = u; heapq.heappush(pq, (dist[v], v))
    path, curr = [], t
    while curr is not None: path.append(curr); curr = parent[curr]
    print("Đường đi:", "->".join(map(str, path[::-1])))
bai_7(g1, 0, 4)