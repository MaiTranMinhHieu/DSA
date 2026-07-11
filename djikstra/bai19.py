import heapq
g_prob = {0: [(1, 0.5), (2, 0.2)], 1: [(3, 0.5)], 2: [(3, 0.9)], 3: []}
def bai_19(g, s, t):
    prob = {n: 0.0 for n in g}; prob[s] = 1.0; pq = [(-1.0, s)]
    while pq:
        p, u = heapq.heappop(pq); p = -p
        if u == t: print(f"Xác suất lớn nhất tới {t}: {p}"); return
        for v, w in g[u]:
            if p * w > prob[v]: prob[v] = p * w; heapq.heappush(pq, (-prob[v], v))
bai_19(g_prob, 0, 3)