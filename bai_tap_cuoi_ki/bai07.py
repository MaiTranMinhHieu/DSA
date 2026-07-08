def dem_mang_con_co_tong_S(A, S):
    dem = 0
    tong_hien_tai = 0
    bang_bam = {0: 1} 
    
    for so in A:
        tong_hien_tai += so
        
        phan_bu = tong_hien_tai - S
        if phan_bu in bang_bam:
            dem += bang_bam[phan_bu]
            
        bang_bam[tong_hien_tai] = bang_bam.get(tong_hien_tai, 0) + 1
        
    return dem

A = [3, 4, 7, 2, -3, 1, 4, 2]
S = 7
print("Câu 7 - Số mảng con có tổng bằng 7:", dem_mang_con_co_tong_S(A, S))