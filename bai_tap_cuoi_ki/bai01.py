def kiem_tra_xe(W, K, tai_trong_thu):
    so_xe = 1
    hang_tren_xe = 0
    
    for kien_hang in W:
        if hang_tren_xe + kien_hang > tai_trong_thu:
            so_xe += 1
            hang_tren_xe = kien_hang
        else:
            hang_tren_xe += kien_hang
            
    return so_xe <= K

def tim_tai_trong_nho_nhat(W, K):
    left = max(W)
    right = sum(W)
    kq = right
    
    while left <= right:
        mid = (left + right) // 2
        if kiem_tra_xe(W, K, mid):
            kq = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return kq

W = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
K = 5
print("Câu 1 - Tải trọng tối thiểu:", tim_tai_trong_nho_nhat(W, K))