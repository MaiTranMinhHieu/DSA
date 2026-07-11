import heapq
g1 = {0: [(1,4), (2,1)], 1: [(3,1)], 2: [(1,2), (3,5), (4,8)], 3: [(4,3), (5,6)], 4: [(5,2), (3,1)], 5: []}
def bai_20(g, s, t, K):
    count = {n: 0 for n in g}; pq = [(0, s)]; res = []
    while pq and count[t] < K:
        d, u = heapq.heappop(pq); count[u] += 1
        if u == t: res.append(d)
        if count[u] <= K:
            for v, w in g[u]: heapq.heappush(pq, (d+w, v))
    print(f"{K} đường đi ngắn nhất tới {t}: {res}")
bai_20(g1, 0, 5, 3)