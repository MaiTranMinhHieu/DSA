def tim_sinh_vien(danh_sach, ma_sv):
    for sv in danh_sach:
        if sv['ma_sv'] == ma_sv:
            print(sv['ma_sv'], sv['ho_ten'], sv['diem_tb'])
            return
    print("Khong tim thay")