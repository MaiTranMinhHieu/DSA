def bellman_ford(dinh, canh, diem_bat_dau):
    khoang_cach = {u: float('inf') for u in dinh}
    khoang_cach[diem_bat_dau] = 0
    
    for _ in range(len(dinh) - 1):
        for u, v, trong_so in canh:
            if khoang_cach[u] + trong_so < khoang_cach[v]:
                khoang_cach[v] = khoang_cach[u] + trong_so
                
    return khoang_cach

dinh = ['A', 'B', 'C']
canh = [('A', 'B', 2), ('A', 'C', 3), ('C', 'B', -2)]
print("Câu 3 - Khoảng cách ngắn nhất từ A (Bellman-Ford):", bellman_ford(dinh, canh, 'A'))