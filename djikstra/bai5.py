import heapq
g_vo_huong = {'A': [('B',5),('C',3)], 'B': [('A',5),('C',1),('D',2)], 'C': [('A',3),('B',1),('D',6)], 'D': [('B',2),('C',6),('E',4)], 'E': [('D',4)]}
def bai_5(g, s):
    dist = {n: float('inf') for n in g}; dist[s] = 0
    pq = [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        for v, w in g[u]:
            if d + w < dist[v]: dist[v] = d + w; heapq.heappush(pq, (dist[v], v))
    print(dist)
bai_5(g_vo_huong, 'A')