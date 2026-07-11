import heapq
g_fuel = {0: [(1, 5, 2), (2, 2, 5)], 1: [(3, 2, 1)], 2: [(3, 1, 1)], 3: []}
def bai_21(g, s, t, fuel):
    pq = [(0, s, fuel)]
    while pq:
        d, u, f = heapq.heappop(pq)
        if u == t: print(f"Chi phí nhỏ nhất với nhiên liệu: {d}"); return
        for v, w, f_cost in g[u]:
            if f >= f_cost: heapq.heappush(pq, (d + w, v, f - f_cost))
bai_21(g_fuel, 0, 3, 3)