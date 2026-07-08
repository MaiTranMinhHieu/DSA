# bai18.py
def demonstrate_negative_edge():
    # Do thi: 0 -> 1 (w=2), 0 -> 2 (w=3), 1 -> 2 (w=-2)
    # Dijkstra se chot dinh 1 (dist=2), sau do chot 2 (dist=3 tu 0).
    # Nhung di qua 1 roi den 2 thi dist chi la 2 - 2 = 0.
    # Dijkstra that bai vi da "chot" dinh 2 voi dist=3 roi.
    
    graph = {
        0: [(1, 2), (2, 3)],
        1: [(2, -2)],
        2: []
    }
    
    print("Dijkstra se sai vi khi da pop dinh khoi min-heap, no khong cap nhat lai toi uu neu co canh am.")
    print("Thuat toan thay the: Bellman-Ford (Duyet tat ca cac canh V-1 lan).")

    # Bellman-Ford demo
    n = 3
    dist = [float('inf')] * n
    dist[0] = 0
    
    edges = [(0, 1, 2), (0, 2, 3), (1, 2, -2)]
    
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                
    print(f"Khoang cach Bellman-Ford tu 0: {dist}")

if __name__ == "__main__":
    demonstrate_negative_edge()